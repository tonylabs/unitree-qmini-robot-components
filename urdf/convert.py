import mujoco
# Load URDF (MuJoCo treats .urdf as XML input)
model = mujoco.MjModel.from_xml_path("Qmini.urdf")
# Export MJCF to XML
mujoco.mj_saveLastXML("qmini.xml", model)
EOF