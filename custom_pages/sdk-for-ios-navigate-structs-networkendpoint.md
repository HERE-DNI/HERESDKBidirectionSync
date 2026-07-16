---
title: "NetworkEndpoint Structure Reference"
slug: "sdk-for-ios-navigate-structs-networkendpoint"
---

# NetworkEndpoint

<div class="declaration">

<div class="language">

``` highlight
public struct NetworkEndpoint : Hashable
```

</div>

</div>

Network endpoint.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15NetworkEndpointV7address0B09IPAddress_pvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-address" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-networkendpoint#sdk-for-ios-navigate-s-7heresdk15NetworkEndpointV7address0B09IPAddress_pvp" class="token"><code>address</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The IP Address of the network endpoint.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var address: IPAddress
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15NetworkEndpointV4ports6UInt16VSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-port" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-networkendpoint#sdk-for-ios-navigate-s-7heresdk15NetworkEndpointV4ports6UInt16VSgvp" class="token"><code>port</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Optional port number of the network endpoint.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var port: UInt16?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15NetworkEndpointV7address4portAC0B09IPAddress_p_s6UInt16VSgtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-address-port" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-networkendpoint#sdk-for-ios-navigate-s-7heresdk15NetworkEndpointV7address4portAC0B09IPAddress_p_s6UInt16VSgtcfc" class="token"><code>init(address:</code><wbr></wbr><code>port:</code><wbr></wbr><code>)</code></a> 

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
  public init(address: IPAddress, port: UInt16?)
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15NetworkEndpointV7addressAC0B09IPAddress_p_tcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-address" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-networkendpoint#sdk-for-ios-navigate-s-7heresdk15NetworkEndpointV7addressAC0B09IPAddress_p_tcfc" class="token"><code>init(address:</code><wbr></wbr><code>)</code></a> 

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
  public init(address: IPAddress)
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15NetworkEndpointV2eeoiySbAC_ACtFZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-_-_" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-networkendpoint#sdk-for-ios-navigate-s-7heresdk15NetworkEndpointV2eeoiySbAC_ACtFZ" class="token"><code>==(_:</code><wbr></wbr><code>_:</code><wbr></wbr><code>)</code></a> 

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
  static func == (lhs: NetworkEndpoint, rhs: NetworkEndpoint) -> Bool
  ```

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

   <span id="sdk-for-ios-navigate-s-7heresdk15NetworkEndpointV4hash4intoys6HasherVz_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-hash-into" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-networkendpoint#sdk-for-ios-navigate-s-7heresdk15NetworkEndpointV4hash4intoys6HasherVz_tF" class="token"><code>hash(into:</code><wbr></wbr><code>)</code></a> 

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
  func hash(into hasher: inout Hasher)
  ```

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

