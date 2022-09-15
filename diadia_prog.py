import streamlit as st

st.title("ONG Exemption app")
criteres = ["Existence d'un plan de réponse humanitaire",
        "Existence d'un appel de fonds pécifique (FICR OU CICR)",
        "Présence de coordinateur ou équipe humanitaire dans le pays (HCT, IDH)",
        "Présence du pays dans la liste OCDE des Etats Fragiles",
        "Pas concerné"]
activites = [" Besoins sanitaires des populations en détresse: lutte contre la mortalité infantile, fournitures de soins élémentaires, recherches scientifiques et programmes d'action en vue de lutter contre les pandémies et les maladies, accès à l'eau",
                " Amélioration des conditions d'hébergement",
                "Element fondamentaux d'éducation indispensables à l'insertion sociale, actions en faveur de la protection et du développement de l'enfant, l'alphabétisation, scolarisation",
                "Actions en faveur des personnes en situations",
                "Actions qui contribuent à la protection des droits des minorités",
                " Actions qui ont pour objet de promouvoir les droits des femmes",
                "Actions de développement permettant l'amorçage d'une activité autonome locale",
                "Pas concerné"]
situations_exceptionnelles = ["Impracticabilité du criblage",
                           "Projet ciblant des mineurs",
                           "Protection de l'identité et des droits humains",
                           "Pas concerné"]


bailleur =st.radio("Quel est le nom de votre bailleur? ",
                   ('AFD', 'CDCS', 'ECHO', 'INTPA', 'AUTRE'))
st.success(bailleur)

if bailleur =='AFD':
    finance = st.radio("Le projet prévoit-il des transferts monétaires et/la mise à disposition de ressources économiquement exploitables?",
             ('OUI', 'NON'))

    if finance == 'OUI':

        critere =st.selectbox(" Le projet répond t'il à un des critères ci dessous? ", criteres)

        if critere!="Pas concerné":
            st.success("Pas de criblage exigé",icon="✅")
        else:
            nature_activites = st.selectbox("Le projet comprend-t-il des activités en lien avec :", activites)

            if nature_activites!="Pas concerné":
                st.success("Pas de criblage exigé, demande d'exemption sur la base de l'annexe 2",icon="✅")
            else:
                situation = st.selectbox("Le projet concerne-t-il les situations ou cas exceptionnels suivants?", situations_exceptionnelles)

                if situation !="Pas concerné":
                    st.success("Pas de criblage exigé, demande d'exemption sur la base de l'annexe 1", icon="✅")

                else:
                    with st.sidebar:
                        seuil_nature = st.slider("Quel est le montant des ressources exploitables par personne et par mois? ",0,500,25 )
                        st.write("Le montant est de",seuil_nature , "euros par mois et par personne")
                        seuil_filet= st.slider ("Quel est le montant des perdiem par personne et par mois? ", 0,500,20)
                        st.write("Le montant est de", seuil_filet, "euros par mois et par personne")

                        if seuil_nature > 100 :
                            st.error("Vous dépassez le seuil des ressources d'exploitation limité à 100 euros par personne et par mois")
                        elif seuil_filet > 50:
                            st.error("Vous dépassez le seuil des Perdiem limité à 50 euros par personne et par mois")
                        else:
                            st.success("Pas de criblage exigé, demande d'exemption sur la base de l'annexe 1", icon="✅")
    else:
        st.success("Pas de criblage exigé, demande d'exemption sur la base de l'annexe 1",icon="✅")

else:
    st.success('Pas de criblage exigé',icon="✅")


