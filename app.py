import streamlit as st
from rdkit import Chem
from rdkit.Chem import Draw, Descriptors, rdMolDescriptors

# Streamlit App Title
st.title("🔬 Molecule Structure Viewer")

# User input for SMILES notation
smiles = st.text_input("Enter a SMILES string:", "CCO")  # Default: Ethanol

# Generate molecule
mol = Chem.MolFromSmiles(smiles)

if mol:
    # Generate image
    img = Draw.MolToImage(mol, size=(200, 200))
    
    # Show molecule image
    st.image(img, caption="Molecular Structure", use_container_width=False)

    # Display molecular properties
    st.write("### 🔍 Molecule Information")
    st.write(f"**Molecular Formula:** {rdMolDescriptors.CalcMolFormula(mol)}")  # Corrected Formula Calculation
    st.write(f"**Molecular Weight:** {Descriptors.ExactMolWt(mol):.2f} g/mol")  # Corrected Molecular Weight Calculation
    st.write(f"**Number of Atoms:** {mol.GetNumAtoms()}")

else:
    st.error("Invalid SMILES string! Please enter a valid molecular representation.")
