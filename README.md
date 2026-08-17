# htop for LoongArch64

<p align="center"><a href="README.md">English</a> | <a href="README-zh.md">中文</a></p>

<p align="center"><img src="https://img.shields.io/badge/htop%20LoongArch64%20%E9%BE%99%E8%8A%AF%E6%9E%B6%E6%9E%84%E5%8F%91%E8%A1%8C%E7%89%88-blue?logo=linux&logoColor=white" alt="htop LoongArch64 龙芯架构发行版"></p>

Build [htop](https://github.com/htop-dev/htop) binaries, RPM, and DEB packages for the **LoongArch64 (loong64)** architecture via CI/CD.

## How it works

A GitHub Actions workflow clones the specified htop version, cross-compiles inside a `linux/loong64` Docker container
via QEMU binfmt emulation, and packages the built binary into RPM and DEB. Target platform: `linux/loong64`.

## Branch naming

Push a branch named `loong64-<htop-version>` (e.g. `loong64-3.5.3`) to trigger a build. Append `+<build>`
(e.g. `loong64-3.5.3+0`) to include build metadata.

## [Release](https://github.com/kubernetes-loong64/htop-loong64/releases)

Push a tag matching `release-loong64-<htop-version>` (e.g. `release-loong64-3.5.3+0`) to publish
a GitHub Release with the built artifacts.

The `+<build>` suffix provides build metadata (e.g. `+0`, `+1-alpha.1`).

The suffix in the build metadata indicates the release stage:

| Suffix  | Stage         |
|---------|---------------|
| `alpha` | Internal beta |
| `beta`  | Public beta   |
| `rc`    | Pre-release   |
| (none)  | Stable        |

## Release artifacts

Each release includes the following files:

| File                                       | Description          |
|--------------------------------------------|----------------------|
| `htop`                                     | htop binary          |
| `htop-<version>-<release>.loongarch64.rpm` | RPM package (Anolis) |
| `htop_<version>-<release>.loong64.deb`     | DEB package (Debian) |

Each file has a corresponding `.asc` detached GPG signature.

## Verifying releases

- Releases are signed with GPG.
- Download the public key from [keys.openpgp.org](https://keys.openpgp.org).
- Fingerprint: [FCF8724722CCBF9F51B1FBE376532BE7E3013105](https://keys.openpgp.org/debug?q=FCF8724722CCBF9F51B1FBE376532BE7E3013105)
- [Manual download](https://keys.openpgp.org/vks/v1/by-fingerprint/FCF8724722CCBF9F51B1FBE376532BE7E3013105)

```shell
gpg --keyserver keys.openpgp.org --recv-keys FCF8724722CCBF9F51B1FBE376532BE7E3013105
echo "FCF8724722CCBF9F51B1FBE376532BE7E3013105:6:" | gpg --import-ownertrust
```

Or download the key file manually and import it:

```shell
gpg --import /tmp/xxx
```

Each release artifact has a corresponding `.asc` detached signature. To verify, download both the file and its `.asc`
signature from the release, then:

```shell
gpg --verify <file>.asc <file>
```

## License

[Apache License 2.0](LICENSE)
