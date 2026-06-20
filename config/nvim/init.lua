vim.wo.number = true;
vim.wo.relativenumber = true;
vim.api.nvim_set_option("clipboard", "unnamedplus")

require("keymaps")
require("plugins")

vim.lsp.enable("lua-language-server")
vim.lsp.enable("pyright")
vim.lsp.enable("nixd")
vim.lsp.enable("rust-analyzer")
