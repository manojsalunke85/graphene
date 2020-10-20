conf = configuration_data()
conf.set('VERSION', meson.project_version())
init_py = configure_file(
    input: '__init__.py.in',
    output: '__init__.py',
    configuration: conf,
)
