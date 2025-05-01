Install `helmfile`

```
export HELMFILE_VERSION=v0.152.0 &&\
curl -sSL "https://github.com/helmfile/helmfile/releases/download/${HELMFILE_VERSION}/helmfile_${HELMFILE_VERSION#v}_linux_amd64.tar.gz" | tar -C /usr/local/bin/ -xzvf - helmfile
```