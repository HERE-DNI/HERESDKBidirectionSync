---
title: "RouteType Enumeration Reference"
slug: "sdk-for-ios-explore-enums-routetype"
---

# RouteType

<div class="declaration">

<div class="language">

``` highlight
public enum RouteType : UInt32, CaseIterable, Codable
```

</div>

</div>

Indicates the level of significance of a route in a range from 1 to 6. A value of 1 stands for the most major route and 6 the most minor. The route type indicates that the road’s name is actually a route number and in many countries is displayed in a shield symbol (e.g., Interstate and State routes in the U.S.). See <https://developer.here.com/documentation/here-map-content-schema/dev_guide/topics_schema/streetname.routetype.html>

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9RouteTypeO11typeUnknownyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-typeUnknown" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-routetype#sdk-for-ios-explore-s-7heresdk9RouteTypeO11typeUnknownyA2CmF" class="token"><code>typeUnknown</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Unknown

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case typeUnknown
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9RouteTypeO10level1RoadyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-level1Road" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-routetype#sdk-for-ios-explore-s-7heresdk9RouteTypeO10level1RoadyA2CmF" class="token"><code>level1Road</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  International / European road

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case level1Road
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9RouteTypeO10level2RoadyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-level2Road" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-routetype#sdk-for-ios-explore-s-7heresdk9RouteTypeO10level2RoadyA2CmF" class="token"><code>level2Road</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  National road

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case level2Road
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9RouteTypeO10level3RoadyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-level3Road" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-routetype#sdk-for-ios-explore-s-7heresdk9RouteTypeO10level3RoadyA2CmF" class="token"><code>level3Road</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Primary road

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case level3Road
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9RouteTypeO10level4RoadyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-level4Road" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-routetype#sdk-for-ios-explore-s-7heresdk9RouteTypeO10level4RoadyA2CmF" class="token"><code>level4Road</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Secondary road

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case level4Road
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9RouteTypeO10level5RoadyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-level5Road" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-routetype#sdk-for-ios-explore-s-7heresdk9RouteTypeO10level5RoadyA2CmF" class="token"><code>level5Road</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Minor road

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case level5Road
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9RouteTypeO10level6RoadyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-level6Road" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-routetype#sdk-for-ios-explore-s-7heresdk9RouteTypeO10level6RoadyA2CmF" class="token"><code>level6Road</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Avenue

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case level6Road
  ```

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

