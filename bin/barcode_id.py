#! /usr/bin/env python
# Copyright 2014 Uri Laserson
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import optparse

import seqtools

import vdj
import vdj.pipeline

parser = optparse.OptionParser()
parser.add_option('-b','--barcodes',dest='barcodes_fasta')
(options, args) = parser.parse_args()

if len(args) == 2:
    inhandle = open(args[0],'r')
    outhandle = open(args[1],'w')
elif len(args) == 1:
    inhandle = open(args[0],'r')
    outhandle = sys.stdout
elif len(args) == 0:
    inhandle = sys.stdin
    outhandle = sys.stdout

# NOTE: all barcodes must be the same length

barcodes = vdj.pipeline.load_barcodes(options.barcodes_fasta)

# iterate through chains
for chain in vdj.parse_imgt(inhandle):
    vdj.pipeline.id_barcode(chain,barcodes)
    print >>outhandle, chain
