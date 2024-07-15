--	 Keybinds	 --
-- 			 --
--    Leader key is " "	 --
-- 			 --
-- z open directory tree --
-- f   fuzzy finder	 --
-- t  open terminal 	 --
-- s save current buffer --


local vim = vim
local execute = vim.api.nvim_command
local fn = vim.fn


-- line numbers
vim.wo.number = true

-- leader key == " "
vim.g.mapleader = " "

-- syntax highlighting
vim.cmd('syntax enable')

-- auto-indentation
vim.cmd('filetype plugin indent on')

-- Highlight current line
vim.wo.cursorline = true

-- Highlight matching parentheses
vim.cmd('set showmatch')

-- line wrapping
vim.wo.wrap = true

-- smart case sensitivity
vim.cmd('set smartcase')

-- incremental search
vim.cmd('set incsearch')

-- persistent undo
vim.cmd('set undofile')

-- auto-save per 0.3s
vim.o.updatetime = 300

-- unfold all folds
vim.opt.foldenable = false

local ensure_packer = function()
  local install_path = fn.stdpath('data')..'/site/pack/packer/start/packer.nvim'
  if fn.empty(fn.glob(install_path)) > 0 then
    fn.system({'git', 'clone', '--depth', '1', 'https://github.com/wbthomason/packer.nvim', install_path})
    vim.cmd [[packadd packer.nvim]]
    return true
  end
  return false
end

local packer_bootstrap = ensure_packer()

require('packer').startup(function(use)
  use 'wbthomason/packer.nvim'
  use 'hrsh7th/nvim-cmp'
  use 'dense-analysis/ale'             -- Linting
  use 'neovim/nvim-lspconfig'
  use {'junegunn/fzf', run = './install --all'} -- Fuzzy finder
  use 'preservim/nerdtree'             -- File explorer
  use 'lervag/vimtex'                  -- LaTex stuff
  use {
	  'nvim-treesitter/nvim-treesitter',
	  run = function()
		  local ts_update = require('nvim-treesitter.install').update({ with_sync = true })
		  ts_update()
	  end,
  }
  use 'hrsh7th/cmp-nvim-lsp'
  use 'hrsh7th/cmp-buffer'
  use 'hrsh7th/cmp-path'
  use 'hrsh7th/cmp-cmdline'
  use 'saadparwaiz1/cmp_luasnip'
  use {
    "L3MON4D3/LuaSnip",
    tag = "v2.3.0", -- Replace <CurrentMajor> by the latest released major (first number of latest release)
    run = "make install_jsregexp"
  }

  -- Theme
  use 'maxmx03/fluoromachine.nvim'

  -- Autopairs
  use {
    "windwp/nvim-autopairs",
    event = "InsertEnter",
    config = function()
      require("nvim-autopairs").setup {}
    end
  }

  -- Status line
  use {
    'hoob3rt/lualine.nvim',
    config = function()
      require('lualine').setup {
        options = {
          icons_enabled = true,
          theme = 'auto',
          component_separators = { left = '', right = '' },
          section_separators = { left = '', right = '' },
          disabled_filetypes = {
            statusline = {},
            winbar = {},
          },
          always_divide_middle = true,
          globalstatus = false,
          refresh = {
            statusline = 1000,
            tabline = 1000,
            winbar = 1000,
          }
        },
        sections = {
          lualine_a = {'mode'},
          lualine_b = {'branch', 'diff', 'diagnostics'},
          lualine_c = {'filename'},
          lualine_x = {'encoding', 'fileformat', 'filetype'},
          lualine_y = {'progress'},
          lualine_z = {'location'}
        },
        inactive_sections = {
          lualine_a = {},
          lualine_b = {},
          lualine_c = {'filename'},
          lualine_x = {'location'},
          lualine_y = {},
          lualine_z = {}
        },
        tabline = {},
        winbar = {},
        inactive_winbar = {},
        extensions = {}
      }
    end
  }
  
  if packer_bootstrap then
    require('packer').sync()
  end
end)

-- Setup nvim-cmp and lspconfig
local cmp = require'cmp'
local lspconfig = require'lspconfig'
local luasnip = require'luasnip'

-- Setup nvim-cmp
cmp.setup({
  snippet = {
    expand = function(args)
      luasnip.lsp_expand(args.body)
    end,
  },
  mapping = {
    ['<C-b>'] = cmp.mapping(cmp.mapping.scroll_docs(-4), { 'i', 'c' }),
    ['<C-f>'] = cmp.mapping(cmp.mapping.scroll_docs(4), { 'i', 'c' }),
    ['<C-Space>'] = cmp.mapping(cmp.mapping.complete(), { 'i', 'c' }),
    ['<C-y>'] = cmp.config.disable,
    ['<C-e>'] = cmp.mapping({
      i = cmp.mapping.abort(),
      c = cmp.mapping.close(),
    }),
    ['<CR>'] = cmp.mapping.confirm({ select = true }),
    ['<Down>'] = cmp.mapping(function(fallback)
      if cmp.visible() then
        cmp.select_next_item()
      elseif luasnip.expand_or_jumpable() then
        luasnip.expand_or_jump()
      else
        fallback()
      end
    end, { 'i', 's' }),
    ['<Up>'] = cmp.mapping(function(fallback)
      if cmp.visible() then
        cmp.select_prev_item()
      elseif luasnip.jumpable(-1) then
        luasnip.jump(-1)
      else
        fallback()
      end
    end, { 'i', 's' }),
  },
  sources = cmp.config.sources({
    { name = 'nvim_lsp' },
    { name = 'luasnip' },
  }, {
    { name = 'buffer' },
    { name = 'path' },
  })
})

-- Use buffer source for `/` and `?`
cmp.setup.cmdline('/', {
  mapping = cmp.mapping.preset.cmdline(),
  sources = {
    { name = 'buffer' }
  }
})

cmp.setup.cmdline('?', {
  mapping = cmp.mapping.preset.cmdline(),
  sources = {
    { name = 'buffer' }
  }
})

---- Use cmdline & path source for ':'
--cmp.setup.cmdline(':', {
--  mapping = cmp.mapping.preset.cmdline(),
--  sources = cmp.config.sources({
--    { name = 'path' }
--  }, {
--    {
--      name = 'cmdline',
--      option = {
--        ignore_cmds = { 'Man', '!' }
--      }
--    }
--  })
--})

-- Setup LSP with capabilities from nvim-cmp
local capabilities = require('cmp_nvim_lsp').default_capabilities()

lspconfig.pyright.setup {
  capabilities = capabilities,
}
	-- Configuring LaTex/VimTex
vim.g.vimtex_view_method = 'general'
vim.g.vimtex_view_general_viewer = 'okular'
vim.g.vimtex_view_general_options = '--unique file:@pdf\\#src:@line@tex'
vim.g.vimtex_compiler_method = 'latexmk'


	-- Setting the colourscheme
local fm = require 'fluoromachine'

fm.setup {
  glow = false,  
  brightness = 0.05,
  theme = 'delta', 
  transparent = false,
  colors = {bg='#120a22', fg='#814698'}, 
  overrides = {},
}

vim.cmd.colorscheme('fluoromachine')

	-- Workaround for NERDTree
-- vim.opt.foldmethod     = 'expr'
-- vim.opt.foldexpr       = 'nvim_treesitter#foldexpr()'
---WORKAROUND
vim.api.nvim_create_autocmd({'BufEnter','BufAdd','BufNew','BufNewFile','BufWinEnter'}, {
  group = vim.api.nvim_create_augroup('TS_FOLD_WORKAROUND', {}),
  callback = function()
    vim.opt.foldmethod     = 'expr'
    vim.opt.foldexpr       = 'nvim_treesitter#foldexpr()'
  end
})
---ENDWORKAROUND


-- Open NERDTree
vim.api.nvim_set_keymap('n', '<Leader>z', ':NERDTreeToggle<CR>', {noremap = true, silent = true})

-- Open Terminal
vim.api.nvim_set_keymap('n', '<leader>t', ':terminal<CR>', {noremap = true, silent = true})

-- Open FZF fuzzy finder
vim.api.nvim_set_keymap('n', '<Leader>f', ':FZF<CR>', {noremap = true, silent = true})

-- Save current buffer
vim.api.nvim_set_keymap('n', '<Leader>s', ':w<CR>', {noremap = true, silent = true})
