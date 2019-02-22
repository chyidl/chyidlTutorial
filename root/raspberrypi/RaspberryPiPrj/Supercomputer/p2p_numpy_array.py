#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# p2p_numpy_array.py
# Supercomputer
#
# 🎂"Here's to the crazy ones. The misfits. The rebels.
# The troublemakers. The round pegs in the square holes.
# The ones who see things differently. They're not found
# of rules. And they have no respect for the status quo.
# You can quote them, disagree with them, glority or vilify
# them. About the only thing you can't do is ignore them.
# Because they change things. They push the human race forward.
# And while some may see them as the creazy ones, we see genius.
# Because the poeple who are crazy enough to think thay can change
# the world, are the ones who do."
#
# Created by Chyi Yaqing on 02/22/19 23:20.
# Copyright © 2019. Chyi Yaqing. All rights reserved.
#
# Distributed under terms of the MIT
import numpy as np
from mpi4py import MPI


comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# passing MPI datatype explicitly
if rank == 0:
    data = np.arange(10, dtype='i')
    print("process %d sends %s" %(rank, data))
    comm.Send([data, MPI.INT], dest=1, tag=77)
elif rank == 1:
    data = np.empty(10, dtype='i')
    comm.Recv([data, MPI.INT], source=0, tag=77)
    print("process %d receives %s" %(rank, data))

# automatic MPI datatype discovery
if rank == 0:
    data = np.arange(10, dtype=np.float64)
    print("process %d sends %s" %(rank, data))
    comm.Send(data, dest=1, tag=13)
elif rank == 1:
    data = np.empty(10, dtype=np.float64)
    comm.Recv(data, source=0, tag=13)
    print("process %d receives %s" %(rank, data))
