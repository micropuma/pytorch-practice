from subprocess import Popen, PIPE

def detect_gpu_version():
    try:
        proc = Popen(
            ["nvidia-smi", "--query-gpu=gpu_name", "--format=csv"],
            stdout = PIPE,
            stderr = PIPE,
        )
        stdout, stderr = proc.communicate()
        stdout = stdout.decode("utf-8")
        sm_names = sm_names = {
            "sm_70": ["V100"],
            "sm_75": ["T4", "Quadro T2000"],
            "sm_80": ["PG509", "A100", "A10", "RTX 30", "A30", "RTX 40", "A16"],
            "sm_90": ["H100"],
        }

        for sm, names in sm_names.items():
            if any(name in stdout for name in names):
                return sm
        return None
    except Exception:
        return None
    
gpu_version = detect_gpu_version()
if gpu_version != None:
    print(gpu_version)