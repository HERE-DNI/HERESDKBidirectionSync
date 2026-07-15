---
title: "Evse Structure Reference"
slug: "sdk-for-ios-explore-structs-evse"
---

# Evse

<div class="declaration">

<div class="language">

``` highlight
public struct Evse : Hashable
```

</div>

</div>

Charge Point Operator (CPO) ID uses the Electric Vehicle Supply Equipment ID (EVSE ID) for an exact identification of the charging infrastructure and charging point.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk4EvseV2idSSSgvp"></span>` `<span id="//apple_ref/swift/Property/id" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evse#/s:7heresdk4EvseV2idSSSgvp" class="token"><code>id</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  HERE ID of the EVSE.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var id: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk4EvseV5cpoIdSSSgvp"></span>` `<span id="//apple_ref/swift/Property/cpoId" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evse#/s:7heresdk4EvseV5cpoIdSSSgvp" class="token"><code>cpoId</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The unique ID of an EVSE in the system of the CPO. This ID is unique in the system of the CPO but not necessarily globally unique. The format will differ between different CPOs. This ID is always provided.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var cpoId: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk4EvseV03cpoB6Emi3IdSSSgvp"></span>` `<span id="//apple_ref/swift/Property/cpoEvseEmi3Id" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evse#/s:7heresdk4EvseV03cpoB6Emi3IdSSSgvp" class="token"><code>cpoEvseEmi3Id</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Identifier in Emi3 format of the EVSE within the Charge Point Operator (CPO) platform. This id is not always present. Example of ID format: `DE*ICT*E0001897`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var cpoEvseEmi3Id: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk4EvseV6statusAA10EVSEStatusOSgvp"></span>` `<span id="//apple_ref/swift/Property/status" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evse#/s:7heresdk4EvseV6statusAA10EVSEStatusOSgvp" class="token"><code>status</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  EVSE status.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var status: EVSEStatus?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk4EvseV11lastUpdated10Foundation4DateVSgvp"></span>` `<span id="//apple_ref/swift/Property/lastUpdated" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evse#/s:7heresdk4EvseV11lastUpdated10Foundation4DateVSgvp" class="token"><code>lastUpdated</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Last update of the dynamic connector availability information.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var lastUpdated: Date?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk4EvseV10connectorsSayAA13EVSEConnectorVGvp"></span>` `<span id="//apple_ref/swift/Property/connectors" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evse#/s:7heresdk4EvseV10connectorsSayAA13EVSEConnectorVGvp" class="token"><code>connectors</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of connectors of this EVSE.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var connectors: [EVSEConnector]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(id: cpoId: cpoEvseEmi3Id: status: lastUpdated: connectors: )

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
  public init ( id : String ? = nil , cpoId : String ? = nil , cpoEvseEmi3Id : String ? = nil , status : EVSEStatus ? = nil , lastUpdated : Date ? = nil , connectors : [ EVSEConnector ] = [])
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-explore-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

