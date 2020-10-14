from . import Exec

# pylint: disable=invalid-name

helloworld = Exec('helloworld', manifest_template='manifest.template')
@helloworld.add_setup
def time_000_helloworld():
    helloworld.run_in_graphene()
time_000_helloworld.setup = helloworld.setup

write_1e4 = Exec('write_1e4', manifest_template='manifest.template')
@write_1e4.add_setup
def time_014_write_1e4():
    write_1e4.run_in_graphene()

write_1e5 = Exec('write_1e5', manifest_template='manifest.template')
@write_1e5.add_setup
def time_015_write_1e5():
    write_1e5.run_in_graphene()

write_1e6 = Exec('write_1e6', manifest_template='manifest.template')
@write_1e6.add_setup
def time_016_write_1e6():
    write_1e6.run_in_graphene()

write_1e7 = Exec('write_1e7', manifest_template='manifest.template')
@write_1e7.add_setup
def time_017_write_1e7():
    write_1e7.run_in_graphene()
