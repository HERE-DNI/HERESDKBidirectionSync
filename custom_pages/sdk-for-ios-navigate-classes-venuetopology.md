---
title: "VenueTopology Class Reference"
slug: "sdk-for-ios-navigate-classes-venuetopology"
---

# VenueTopology

<div class="declaration">

<div class="language">

``` highlight
public class VenueTopology
```

``` highlight
extension VenueTopology: NativeBase
```

``` highlight
extension VenueTopology: Hashable
```

</div>

</div>

Represents routing topologies inside the <a href="sdk-for-ios-navigate-classes-venuelevel">`VenueLevel`</a>. The topologies can be paths used for enabling routing services.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13VenueTopologyC25AccessCharacteristicsLista"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Alias-AccessCharacteristicsList" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-venuetopology#sdk-for-ios-navigate-s-7heresdk13VenueTopologyC25AccessCharacteristicsLista" class="token"><code>AccessCharacteristicsList</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Undocumented

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias AccessCharacteristicsList = [VenueTopology.AccessCharacteristics]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-venuetopology-accesscharacteristics">AccessCharacteristics</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13VenueTopologyC10identifierSSvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-identifier" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-venuetopology#sdk-for-ios-navigate-s-7heresdk13VenueTopologyC10identifierSSvp" class="token"><code>identifier</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The `id` of the topology.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var identifier: String { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13VenueTopologyC5levelAA0B5LevelCvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-level" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-venuetopology#sdk-for-ios-navigate-s-7heresdk13VenueTopologyC5levelAA0B5LevelCvp" class="token"><code>level</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The parent level of the topology.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var level: VenueLevel { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-venuelevel">VenueLevel</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13VenueTopologyC13accessibilitySayAC21AccessCharacteristicsCGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-accessibility" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-venuetopology#sdk-for-ios-navigate-s-7heresdk13VenueTopologyC13accessibilitySayAC21AccessCharacteristicsCGvp" class="token"><code>accessibility</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of <a href="sdk-for-ios-navigate-classes-venuetopology-accesscharacteristics">`VenueTopology.AccessCharacteristics`</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var accessibility: VenueTopology.AccessCharacteristicsList { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-venuetopology#sdk-for-ios-navigate-s-7heresdk13VenueTopologyC25AccessCharacteristicsLista">AccessCharacteristicsList</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13VenueTopologyC21AccessCharacteristicsC"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Class-AccessCharacteristics" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-venuetopology#sdk-for-ios-navigate-s-7heresdk13VenueTopologyC21AccessCharacteristicsC" class="token"><code>AccessCharacteristics</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the access characreisticas of a topology. Access characteristics is a combination of <a href="sdk-for-ios-navigate-enums-venuetransportmode">`VenueTransportMode`</a> which is suppoted on this topology and the <a href="sdk-for-ios-navigate-classes-venuetopology-topologydirectionality">`VenueTopology.TopologyDirectionality`</a> towards which it is allowed.

  <a href="sdk-for-ios-navigate-classes-venuetopology-accesscharacteristics" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class AccessCharacteristics
  ```

  ``` highlight
  extension VenueTopology.AccessCharacteristics: NativeBase
  ```

  ``` highlight
  extension VenueTopology.AccessCharacteristics: Hashable
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-venuetopology">VenueTopology</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13VenueTopologyC0C14DirectionalityO"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Enum-TopologyDirectionality" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-venuetopology#sdk-for-ios-navigate-s-7heresdk13VenueTopologyC0C14DirectionalityO" class="token"><code>TopologyDirectionality</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Available directions.

  <a href="sdk-for-ios-navigate-classes-venuetopology-topologydirectionality" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum TopologyDirectionality : UInt32, CaseIterable, Codable
  ```

  </div>

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

