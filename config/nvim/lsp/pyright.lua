---@type vim.lsp.Config
return {
  cmd = { 'pyright-langserver', '--stdio' },
  filetypes = { 'python' },
  root_markers = {
    'pyproject.toml',
    'requirements.txt',
    'config.py',
  }
}
