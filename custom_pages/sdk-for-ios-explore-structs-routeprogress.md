---
title: "RouteProgress Structure Reference"
slug: "sdk-for-ios-explore-structs-routeprogress"
---

# RouteProgress

<div class="declaration">

<div class="language">

``` highlight
public struct RouteProgress : Hashable
```

</div>

</div>

Contains all the relevant information on the user’s progress along a route.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk13RouteProgressV12sectionIndexs5Int32Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-sectionIndex" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-routeprogress#sdk-for-ios-explore-s-7heresdk13RouteProgressV12sectionIndexs5Int32Vvp" class="token"><code>sectionIndex</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Index of the <a href="sdk-for-ios-explore-classes-section">`Section`</a> in the route. Note that this section index does not point to the current <a href="sdk-for-ios-explore-structs-sectionprogress">`SectionProgress`</a> but to the route <a href="sdk-for-ios-explore-classes-section">`Section`</a> that you can access via `route` and <a href="sdk-for-ios-explore-classes-route#sdk-for-ios-explore-s-7heresdk5RouteC8sectionsSayAA7SectionCGvp">`Route.sections`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.27.0. Use `RouteProgress.routeMatchedLocation` instead.")
  public var sectionIndex: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk13RouteProgressV9spanIndexs5Int32Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-spanIndex" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-routeprogress#sdk-for-ios-explore-s-7heresdk13RouteProgressV9spanIndexs5Int32Vvp" class="token"><code>spanIndex</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Index of the <a href="sdk-for-ios-explore-classes-span">`Span`</a> in the route section.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.27.0. Use `RouteProgress.routeMatchedLocation` instead.")
  public var spanIndex: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk13RouteProgressV07sectionC0SayAA07SectionC0VGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-sectionProgress" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-routeprogress#sdk-for-ios-explore-s-7heresdk13RouteProgressV07sectionC0SayAA07SectionC0VGvp" class="token"><code>sectionProgress</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The progress for each <a href="sdk-for-ios-explore-classes-section">`Section`</a> from the current one to the last one. Note that the progress information is accumulated successively, therefore information relative to the final destination is in the last item of the list. The list is guaranteed to be non-empty.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var sectionProgress: [SectionProgress]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-sectionprogress">SectionProgress</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk13RouteProgressV08maneuverC0SayAA08ManeuverC0VGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-maneuverProgress" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-routeprogress#sdk-for-ios-explore-s-7heresdk13RouteProgressV08maneuverC0SayAA08ManeuverC0VGvp" class="token"><code>maneuverProgress</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The progress for next and next-next maneuvers (see <a href="sdk-for-ios-explore-classes-maneuver">`Maneuver`</a>). Note that the list can contain at maximum two items (for next and next-next maneuvers) and one or zero when approaching the destination.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var maneuverProgress: [ManeuverProgress]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-maneuverprogress">ManeuverProgress</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk13RouteProgressV20routeMatchedLocationAA0beF0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-routeMatchedLocation" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-routeprogress#sdk-for-ios-explore-s-7heresdk13RouteProgressV20routeMatchedLocationAA0beF0Vvp" class="token"><code>routeMatchedLocation</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Route matched location.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var routeMatchedLocation: RouteMatchedLocation
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-routematchedlocation">RouteMatchedLocation</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk13RouteProgressV07sectionC008maneuverC020routeMatchedLocationACSayAA07SectionC0VG_SayAA08ManeuverC0VGAA0bgH0Vtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-sectionProgress-maneuverProgress-routeMatchedLocation" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-routeprogress#sdk-for-ios-explore-s-7heresdk13RouteProgressV07sectionC008maneuverC020routeMatchedLocationACSayAA07SectionC0VG_SayAA08ManeuverC0VGAA0bgH0Vtcfc" class="token"><code>init(sectionProgress:</code><wbr></wbr><code>maneuverProgress:</code><wbr></wbr><code>routeMatchedLocation:</code><wbr></wbr><code>)</code></a> 

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
  public init(sectionProgress: [SectionProgress], maneuverProgress: [ManeuverProgress], routeMatchedLocation: RouteMatchedLocation = RouteMatchedLocation())
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-sectionprogress">SectionProgress</a>
  - <a href="sdk-for-ios-explore-structs-maneuverprogress">ManeuverProgress</a>
  - <a href="sdk-for-ios-explore-structs-routematchedlocation">RouteMatchedLocation</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk13RouteProgressV12sectionIndex04spanE00dC008maneuverC020routeMatchedLocationACs5Int32V_AJSayAA07SectionC0VGSayAA08ManeuverC0VGAA0biJ0Vtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-sectionIndex-spanIndex-sectionProgress-maneuverProgress-routeMatchedLocation" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-routeprogress#sdk-for-ios-explore-s-7heresdk13RouteProgressV12sectionIndex04spanE00dC008maneuverC020routeMatchedLocationACs5Int32V_AJSayAA07SectionC0VGSayAA08ManeuverC0VGAA0biJ0Vtcfc" class="token"><code>init(sectionIndex:</code><wbr></wbr><code>spanIndex:</code><wbr></wbr><code>sectionProgress:</code><wbr></wbr><code>maneuverProgress:</code><wbr></wbr><code>routeMatchedLocation:</code><wbr></wbr><code>)</code></a> 

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
  @available(*, deprecated)
  public init(sectionIndex: Int32 = 0, spanIndex: Int32 = 0, sectionProgress: [SectionProgress], maneuverProgress: [ManeuverProgress], routeMatchedLocation: RouteMatchedLocation = RouteMatchedLocation())
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-sectionprogress">SectionProgress</a>
  - <a href="sdk-for-ios-explore-structs-maneuverprogress">ManeuverProgress</a>
  - <a href="sdk-for-ios-explore-structs-routematchedlocation">RouteMatchedLocation</a>

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

