# -*- coding: utf-8 -*-
from tutorial import tools
from tutorial.utils.dashbio_docs import create_doc_page, get_component_names

component_names = get_component_names('dash_bio')

examples = {
    'alignment-chart': tools.load_example(
        'tutorial/examples/dashbio_components/alignment_chart.py'),
    'sequence-viewer': tools.load_example(
        'tutorial/examples/dashbio_components/sequence_viewer.py'),
    'clustergram': tools.load_example(
        'tutorial/examples/dashbio_components/clustergram.py'),
    'speck': tools.load_example(
        'tutorial/examples/dashbio_components/speck.py'),
    'circos': tools.load_example(
        'tutorial/examples/dashbio_components/circos.py'),
    'ideogram': tools.load_example(
        'tutorial/examples/dashbio_components/ideogram.py')
}




# AlignmentChart/AlignmentViewer
AlignmentChart = create_doc_page(examples, component_names, 'alignment-chart')

# Circos
Circos = create_doc_page(examples, component_names, 'circos')

# Clustergram
Clustergram = create_doc_page(examples, component_names, 'clustergram')

# Ideogram
Ideogram = create_doc_page(examples, component_names, 'ideogram')

# ManhattanPlot

# Molecule3dViewer

# NeedlePlot

# OncoPrint

# SequenceViewer
SequenceViewer = create_doc_page(examples, component_names, 'sequence-viewer')

# Speck
Speck = create_doc_page(examples, component_names, 'speck')

# VolcanoPlot
