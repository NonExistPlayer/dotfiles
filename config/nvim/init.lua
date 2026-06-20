vim.wo.number = true;
vim.wo.relativenumber = true;

require("keymaps")
require("plugins")

vim.lsp.enable("lua-language-server")
vim.lsp.enable("pyright")
vim.lsp.enable("nixd")
vim.lsp.enable("rust-analyzer")
