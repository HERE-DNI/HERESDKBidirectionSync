---
title: "LocalizedRoadNumber Structure Reference"
slug: "sdk-for-ios-explore-structs-localizedroadnumber"
---

# LocalizedRoadNumber

<div class="declaration">

<div class="language">

``` highlight
public struct LocalizedRoadNumber : Hashable
```

</div>

</div>

Used to represent road number localized to specific language with optional direction and route type information.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19LocalizedRoadNumberV09localizedD0AA0B4TextVvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-localizedNumber" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-localizedroadnumber#sdk-for-ios-explore-s-7heresdk19LocalizedRoadNumberV09localizedD0AA0B4TextVvp" class="token"><code>localizedNumber</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Road number with locale information.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var localizedNumber: LocalizedText
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-localizedtext">LocalizedText</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19LocalizedRoadNumberV9directionAA17CardinalDirectionOSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-direction" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-localizedroadnumber#sdk-for-ios-explore-s-7heresdk19LocalizedRoadNumberV9directionAA17CardinalDirectionOSgvp" class="token"><code>direction</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Road direction. This property indicates the official directional identifier assigned to highways. Can be `nil` when direction is not assigned to highways. The direction indicates the same information as on the signpost shield: For example, if is “101 West”, the directions contains WEST. Note that the official direction is not necessarily the travel direction. For example, US-101 through the city of Sunnyvale is physically located East to West. However, the official direction on sign is North/South.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var direction: CardinalDirection?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-cardinaldirection">CardinalDirection</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19LocalizedRoadNumberV9routeTypeAA05RouteF0Ovp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-routeType" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-localizedroadnumber#sdk-for-ios-explore-s-7heresdk19LocalizedRoadNumberV9routeTypeAA05RouteF0Ovp" class="token"><code>routeType</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The route type of the LocalizedRoadNumber.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var routeType: RouteType
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-routetype">RouteType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19LocalizedRoadNumberV09localizedD09direction9routeTypeAcA0B4TextV_AA17CardinalDirectionOSgAA05RouteH0Otcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-localizedNumber-direction-routeType" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-localizedroadnumber#sdk-for-ios-explore-s-7heresdk19LocalizedRoadNumberV09localizedD09direction9routeTypeAcA0B4TextV_AA17CardinalDirectionOSgAA05RouteH0Otcfc" class="token"><code>init(localizedNumber:</code><wbr></wbr><code>direction:</code><wbr></wbr><code>routeType:</code><wbr></wbr><code>)</code></a> 

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
  public init(localizedNumber: LocalizedText, direction: CardinalDirection? = nil, routeType: RouteType)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-localizedtext">LocalizedText</a>
  - <a href="sdk-for-ios-explore-enums-cardinaldirection">CardinalDirection</a>
  - <a href="sdk-for-ios-explore-enums-routetype">RouteType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19LocalizedRoadNumberV08completecD0SSyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-completeRoadNumber" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-localizedroadnumber#sdk-for-ios-explore-s-7heresdk19LocalizedRoadNumberV08completecD0SSyF" class="token"><code>completeRoadNumber()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns the whole road number information including its cardinal direction. In case direction is empty, the original localized text will be returned.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func completeRoadNumber() -> String
  ```

  </div>

  </div>

  <div>

  #### Return Value

  The whole road number information including its cardinal direction.

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

