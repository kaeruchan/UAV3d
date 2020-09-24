from gym.envs.registration import register

register(
    id='UAV3D-v0',
    entry_point='UAV3D.envs.uav_3d:UAV3D'
)
