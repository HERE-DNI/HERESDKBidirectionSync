---
title: "ProxySettings Structure Reference"
slug: "sdk-for-ios-navigate-structs-proxysettings"
---

# ProxySettings

<div class="declaration">

<div class="language">

``` highlight
public struct ProxySettings : Hashable
```

</div>

</div>

Proxy configuration for the HERE SDK network that is applied per request. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk13ProxySettingsV4typeAC0B4TypeOvp"></span>` `<span id="//apple_ref/swift/Property/type" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-proxysettings#/s:7heresdk13ProxySettingsV4typeAC0B4TypeOvp" class="token"><code>type</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the type of the proxy server.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var type: ProxySettings.ProxyType
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13ProxySettingsV9ipAddress7Network9IPAddress_pvp"></span>` `<span id="//apple_ref/swift/Property/ipAddress" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-proxysettings#/s:7heresdk13ProxySettingsV9ipAddress7Network9IPAddress_pvp" class="token"><code>ipAddress</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the IP Address of the proxy server.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var ipAddress: IPAddress
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13ProxySettingsV4ports6UInt16Vvp"></span>` `<span id="//apple_ref/swift/Property/port" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-proxysettings#/s:7heresdk13ProxySettingsV4ports6UInt16Vvp" class="token"><code>port</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the port number of the proxy server.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var port: UInt16
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13ProxySettingsV11credentialsAC11CredentialsVSgvp"></span>` `<span id="//apple_ref/swift/Property/credentials" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-proxysettings#/s:7heresdk13ProxySettingsV11credentialsAC11CredentialsVSgvp" class="token"><code>credentials</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Optional field to define credentials to authenticate a user to the proxy server.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var credentials: ProxySettings.Credentials?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(type: ipAddress: port: credentials: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( type : ProxySettings . ProxyType , ipAddress : IPAddress , port : UInt16 , credentials : ProxySettings . Credentials ? = nil )
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13ProxySettingsV0B4TypeO"></span>` `<span id="//apple_ref/swift/Enum/ProxyType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-proxysettings#/s:7heresdk13ProxySettingsV0B4TypeO" class="token"><code>ProxyType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Supported types of proxy connection.

  <a href="sdk-for-ios-navigate-structs-proxysettings-proxytype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum ProxyType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13ProxySettingsV11CredentialsV"></span>` `<span id="//apple_ref/swift/Struct/Credentials" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-proxysettings#/s:7heresdk13ProxySettingsV11CredentialsV" class="token"><code>Credentials</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Authentication data

  <a href="sdk-for-ios-navigate-structs-proxysettings-credentials" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct Credentials : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      ==(_: _: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Compare objects

  - Return true if objects are equal, false otherwise.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  static func == ( lhs : ProxySettings , rhs : ProxySettings ) -> Bool
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>lhs</code></em><code> </code></td>
  <td><div>
  <p>First object to compare</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>rhs</code></em><code> </code></td>
  <td><div>
  <p>Second object to compare</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      hash(into: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Hashes object

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func hash ( into hasher : inout Hasher )
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>hasher</code></em><code> </code></td>
  <td><div>
  <p>The hasher</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-navigate-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

