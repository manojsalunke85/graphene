install_data('../Pal/src/host/Linux/libpal.so',
    install_dir: pkglibexecdir / 'linux')
install_subdir('../Pal/src/host/Linux/gdb_integration',
    install_dir: pkglibexecdir / 'linux')

install_data(
    '../Pal/src/host/Linux-SGX/pal-sgx',
    '../Pal/src/host/Linux-SGX/libpal.so',
    install_dir: pkglibexecdir / 'linux-sgx')
install_subdir('../Pal/src/host/Linux-SGX/gdb_integration',
    install_dir: pkglibexecdir / 'linux-sgx')

conf = configuration_data()
conf.set_quoted('IN_GIT', '')

hostpalpath_linux = prefix / pkglibexecdir / 'linux'
conf_graphene = configuration_data()
conf_graphene.merge_from(conf)
conf_graphene.set('SGX', 0)
conf_graphene.set_quoted('HOST_PAL_PATH', hostpalpath_linux)
conf_graphene.set_quoted('LIBPAL_PATH', hostpalpath_linux / 'libpal.so')
conf_graphene.set_quoted('PAL_CMD', hostpalpath_linux / 'libpal.so')

configure_file(
    input: 'pal_loader',
    output: 'graphene',
    configuration: conf_graphene,
    install_dir: get_option('bindir'),
)

hostpalpath_linux_sgx = prefix / pkglibexecdir / 'linux-sgx'
conf_graphene_sgx = configuration_data()
conf_graphene_sgx.merge_from(conf)
conf_graphene_sgx.set('SGX', 1)
conf_graphene_sgx.set_quoted('HOST_PAL_PATH', hostpalpath_linux_sgx)
conf_graphene_sgx.set_quoted('LIBPAL_PATH', hostpalpath_linux_sgx / 'libpal.so')
conf_graphene_sgx.set_quoted('PAL_CMD', hostpalpath_linux_sgx / 'pal-sgx')

configure_file(
    input: 'pal_loader',
    output: 'graphene-sgx',
    configuration: conf_graphene_sgx,
    install_dir: get_option('bindir'),
)
