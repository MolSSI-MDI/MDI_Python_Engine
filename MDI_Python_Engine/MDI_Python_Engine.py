import mdi

try:
    from mpi4py import MPI
    use_mpi4py = True
except ImportError:
    use_mpi4py = False

# Get the MPI communicator
if use_mpi4py:
    mpi_world = MPI.COMM_WORLD
else:
    mpi_world = None



if __name__ == "__main__":
    print("Hello World!")

    # Ensure that all ranks have terminated
    if use_mpi4py:
        MPI.COMM_WORLD.Barrier()
