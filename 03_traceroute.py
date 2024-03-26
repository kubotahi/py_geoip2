import subprocess
import platform


command = "traceroute"

# 宛先のIPアドレスまたはホスト名
target = "8.8.8.8"

# コマンドを実行
try:
    output = subprocess.run([command, target], capture_output=True, text=True, check=True)
    print(output.stdout)
except subprocess.CalledProcessError as e:
    print(f"Error executing {command}: {e}")


