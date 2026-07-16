---
title: "FunctionalRoadClassZoomPolicyOptions Structure Reference"
slug: "sdk-for-ios-explore-classes-trackingcamerabehavior-functionalroadclasszoompolicyoptions"
---

# FunctionalRoadClassZoomPolicyOptions

<div class="declaration">

<div class="language">

``` highlight
public struct FunctionalRoadClassZoomPolicyOptions
```

</div>

</div>

Configuration for mapping functional road classes to zoom levels. For correct default initialization, use <a href="sdk-for-ios-explore-classes-trackingcamerabehavior#sdk-for-ios-explore-s-7heresdk22TrackingCameraBehaviorC43defaultFunctionalRoadClassZoomPolicyOptionsAC0fghijK0VyFZ">`TrackingCameraBehavior.defaultFunctionalRoadClassZoomPolicyOptions(...)`</a>.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22TrackingCameraBehaviorC36FunctionalRoadClassZoomPolicyOptionsV07defaultH0AA10MapMeasureVvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-defaultZoom" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-trackingcamerabehavior-functionalroadclasszoompolicyoptions#sdk-for-ios-explore-s-7heresdk22TrackingCameraBehaviorC36FunctionalRoadClassZoomPolicyOptionsV07defaultH0AA10MapMeasureVvp" class="token"><code>defaultZoom</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Default zoom returned when the functional road class is missing or unmapped. Defaults to a <a href="sdk-for-ios-explore-structs-mapmeasure">`MapMeasure`</a> with kind <a href="sdk-for-ios-explore-structs-mapmeasure-kind#sdk-for-ios-explore-s-7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">`MapMeasure.Kind.zoomLevel`</a> and value 16.5.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var defaultZoom: MapMeasure
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-mapmeasure">MapMeasure</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22TrackingCameraBehaviorC36FunctionalRoadClassZoomPolicyOptionsV010functionalfg2ToH0SDyAA0efG0OAA10MapMeasureVGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-functionalRoadClassToZoom" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-trackingcamerabehavior-functionalroadclasszoompolicyoptions#sdk-for-ios-explore-s-7heresdk22TrackingCameraBehaviorC36FunctionalRoadClassZoomPolicyOptionsV010functionalfg2ToH0SDyAA0efG0OAA10MapMeasureVGvp" class="token"><code>functionalRoadClassToZoom</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Maps each functional road class to the zoom that should be used for it. If <a href="sdk-for-ios-explore-classes-trackingcamerabehavior#sdk-for-ios-explore-s-7heresdk22TrackingCameraBehaviorC43defaultFunctionalRoadClassZoomPolicyOptionsAC0fghijK0VyFZ">`TrackingCameraBehavior.defaultFunctionalRoadClassZoomPolicyOptions(...)`</a> is not used for `TrackingCameraBehavior.FunctionalRoadClassZoomPolicyOptions`, it will be an empty map.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var functionalRoadClassToZoom: [FunctionalRoadClass : MapMeasure]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-functionalroadclass">FunctionalRoadClass</a>
  - <a href="sdk-for-ios-explore-structs-mapmeasure">MapMeasure</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22TrackingCameraBehaviorC36FunctionalRoadClassZoomPolicyOptionsV07defaultH0010functionalfg2ToH0AeA10MapMeasureV_SDyAA0efG0OAIGtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-defaultZoom-functionalRoadClassToZoom" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-trackingcamerabehavior-functionalroadclasszoompolicyoptions#sdk-for-ios-explore-s-7heresdk22TrackingCameraBehaviorC36FunctionalRoadClassZoomPolicyOptionsV07defaultH0010functionalfg2ToH0AeA10MapMeasureV_SDyAA0efG0OAIGtcfc" class="token"><code>init(defaultZoom:</code><wbr></wbr><code>functionalRoadClassToZoom:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance.

  Note: This is a beta feature; there maybe bugs and unexpected behavior. Related API’s are subject to change without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(defaultZoom: MapMeasure = MapMeasure(kind: MapMeasure.Kind.zoomLevel, value: 16.5), functionalRoadClassToZoom: [FunctionalRoadClass : MapMeasure] = [:])
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-trackingcamerabehavior-functionalroadclasszoompolicyoptions#sdk-for-ios-explore-s-7heresdk22TrackingCameraBehaviorC36FunctionalRoadClassZoomPolicyOptionsV07defaultH0AA10MapMeasureVvp">defaultZoom</a>
  - <a href="sdk-for-ios-explore-structs-mapmeasure">MapMeasure</a>
  - <a href="sdk-for-ios-explore-enums-functionalroadclass">FunctionalRoadClass</a>

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

