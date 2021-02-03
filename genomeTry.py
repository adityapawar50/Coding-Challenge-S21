from reportlab.lib import colors 
from reportlab.lib.units import cm 
from Bio.Graphics import GenomeDiagram
from Bio import SeqIO
from Bio.SeqFeature import SeqFeature, FeatureLocation

record = SeqIO.read("Genome.gb", "genbank")

#creates diagram and adds feature track
gd_diagram = GenomeDiagram.Diagram(record.id)
gd_track_for_features = gd_diagram.new_track(1, name="Annotated Features")

gd_feature_set = gd_track_for_features.new_set()



# for the feature sets color to altenrate between genomic variants and adds arrows for direction
for feature in record.features:
    if feature.type != "gene":
        #Exclude this feature
        continue
    if len(gd_feature_set) % 2 == 0:
        color = colors.red
    else:
        color = colors.lightblue
        
    gd_feature_set.add_feature(feature, sigil="ARROW",
                               color=color, label=True,
                               label_size = 14, label_angle=0)       




#draws diagram to file

gd_diagram.draw(format="circular", circular=True, pagesize=(20*cm,20*cm),
                start=0, end=len(record), circle_core = 0.5)
gd_diagram.write("genome_circular.png", "PNG")

