import streamlit as st
import expTwo
import check

st.set_page_config(page_title='Exp Two', page_icon="👾")


PAGES = {
    "Circuit Setup": check,
    "Observations": expTwo
}

st.header('VSWR Measurement and Bandwidth measurement')
st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed dapibus ligula rhoncus risus vestibulum ullamcorper. Aenean molestie est a fringilla facilisis. Integer mattis, risus eget ornare imperdiet, felis mi eleifend purus, sit amet porta lorem nulla id massa. Praesent commodo turpis ut nibh convallis, eu aliquam justo cursus. Aliquam ut sodales mauris. Fusce tempus, nisi eget ullamcorper semper, tellus augue egestas nibh, nec scelerisque elit libero non nisl. Nulla imperdiet, neque eu luctus congue, tortor augue tincidunt nulla, laoreet aliquam lacus metus ut magna. Proin placerat ac eros a luctus. Praesent venenatis nulla sit amet urna fringilla convallis.")

st.write("In hac habitasse platea dictumst. Cras et urna mi. Vivamus rutrum diam in odio egestas laoreet. Pellentesque venenatis malesuada ultricies. Donec faucibus laoreet molestie. Aliquam vestibulum aliquet eros, non tristique velit tempor ut. Fusce mattis, urna nec varius imperdiet, augue ipsum dictum elit, fringilla consectetur nisi metus sed diam. Nulla posuere suscipit dictum. Fusce vitae leo sodales, euismod lectus a, viverra ex. Ut iaculis hendrerit nibh, vel pretium tellus accumsan in. Nulla mollis enim tristique blandit tristique. Aliquam eget purus in massa lobortis blandit sit amet eget lacus. Quisque ac nunc libero. Vivamus in est eu leo efficitur elementum.")

st.write("Ut sit amet felis vel mi tempor aliquet a eget lacus. Etiam sodales eros fermentum lacus volutpat facilisis. Duis fringilla scelerisque felis, vel viverra mauris eleifend ut. Aenean hendrerit leo at eros malesuada, quis tempus velit blandit. Aenean pretium diam urna, vitae eleifend est ultrices sed. Proin hendrerit molestie turpis, sed dignissim mi pellentesque at. Nulla ornare volutpat nisi pellentesque ullamcorper. Donec tristique posuere mattis. Aenean fringilla blandit diam, nec tempor mi pulvinar a. Nam eu tristique nisi. Duis efficitur mi sapien, sit amet feugiat felis tempus quis. Proin in ex malesuada, varius tellus a, gravida sapien. Etiam viverra arcu purus, vestibulum tempus nunc semper at. Nullam posuere tempus velit et aliquam. Donec fringilla, ex et elementum elementum, augue arcu aliquet massa, a eleifend enim orci malesuada lacus. Praesent ut vestibulum ante.")

st.write("Maecenas eleifend sem sed turpis commodo, et dapibus mi mattis. Sed et sem quis massa egestas fermentum eu nec urna. Etiam varius suscipit tortor, sed mollis neque pretium ac. Aenean faucibus purus sed lacus dapibus, sit amet mollis lorem mollis. Nullam sed consectetur velit, at feugiat purus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque eu nisl erat. Cras et congue dui. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Nam quis lacus ut sapien malesuada ullamcorper vel ac risus. Nunc vel fringilla lacus. Sed tempus efficitur erat, nec interdum elit mattis convallis.")

st.sidebar.title("Experiment - Two")
selection = st.sidebar.radio("Go To", list(PAGES.keys()))
page = PAGES[selection]
page.showDet()
