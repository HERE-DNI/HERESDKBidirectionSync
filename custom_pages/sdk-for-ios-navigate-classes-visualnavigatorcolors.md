---
title: "VisualNavigatorColors Class Reference"
slug: "sdk-for-ios-navigate-classes-visualnavigatorcolors"
---

# VisualNavigatorColors

<div class="declaration">

<div class="language">

``` highlight
public class VisualNavigatorColors
```

``` highlight
extension VisualNavigatorColors: NativeBase
```

``` highlight
extension VisualNavigatorColors: Hashable
```

</div>

</div>

This class contains colors used by <a href="sdk-for-ios-navigate-classes-visualnavigator">`VisualNavigator`</a> to render the route and the maneuver arrow visualization.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk21VisualNavigatorColorsC18maneuverArrowColorSo7UIColorCvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-maneuverArrowColor" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-visualnavigatorcolors#sdk-for-ios-navigate-s-7heresdk21VisualNavigatorColorsC18maneuverArrowColorSo7UIColorCvp" class="token"><code>maneuverArrowColor</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Maneuver arrow color. The object containing color used to draw maneuver arrows on the route to highlight lane directions at the end of a street. The alpha channel is ignored. The color is interpreted as fully opaque.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var maneuverArrowColor: UIColor { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk21VisualNavigatorColorsC014trafficOnRouteD0AA07TrafficfgD0Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-trafficOnRouteColors" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-visualnavigatorcolors#sdk-for-ios-navigate-s-7heresdk21VisualNavigatorColorsC014trafficOnRouteD0AA07TrafficfgD0Vvp" class="token"><code>trafficOnRouteColors</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Colors used to visualize traffic conditions on the route ahead of the current location, for segments with a jam factor of 4.0 or higher. For route segments with a jam factor below 4.0 and those behind the current location, <a href="sdk-for-ios-navigate-structs-routeprogresscolors">`RouteProgressColors`</a> are used instead.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var trafficOnRouteColors: TrafficOnRouteColors { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-trafficonroutecolors">TrafficOnRouteColors</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk21VisualNavigatorColorsC016setRouteProgressD020sectionTransportMode05routegD0yAA07SectioniJ0O_AA0fgD0VtF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-setRouteProgressColors-sectionTransportMode-routeProgressColors" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-visualnavigatorcolors#sdk-for-ios-navigate-s-7heresdk21VisualNavigatorColorsC016setRouteProgressD020sectionTransportMode05routegD0yAA07SectioniJ0O_AA0fgD0VtF" class="token"><code>setRouteProgressColors(sectionTransportMode:</code><wbr></wbr><code>routeProgressColors:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets route color for visualization.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setRouteProgressColors(sectionTransportMode: SectionTransportMode, routeProgressColors: RouteProgressColors)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-sectiontransportmode">SectionTransportMode</a>
  - <a href="sdk-for-ios-navigate-structs-routeprogresscolors">RouteProgressColors</a>

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
  <td><code> </code><em><code>sectionTransportMode</code></em><code> </code></td>
  <td><div>
  <p>The section transport mode.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>routeProgressColors</code></em><code> </code></td>
  <td><div>
  <p>The route progress colors.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk21VisualNavigatorColorsC016getRouteProgressD020sectionTransportModeAA0fgD0VAA07SectioniJ0O_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-getRouteProgressColors-sectionTransportMode" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-visualnavigatorcolors#sdk-for-ios-navigate-s-7heresdk21VisualNavigatorColorsC016getRouteProgressD020sectionTransportModeAA0fgD0VAA07SectioniJ0O_tF" class="token"><code>getRouteProgressColors(sectionTransportMode:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gets route color for visualization.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getRouteProgressColors(sectionTransportMode: SectionTransportMode) -> RouteProgressColors
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-sectiontransportmode">SectionTransportMode</a>
  - <a href="sdk-for-ios-navigate-structs-routeprogresscolors">RouteProgressColors</a>

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
  <td><code> </code><em><code>sectionTransportMode</code></em><code> </code></td>
  <td><div>
  <p>The section transport mode.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The route color for visualization.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk21VisualNavigatorColorsC03dayD0ACyFZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-dayColors" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-visualnavigatorcolors#sdk-for-ios-navigate-s-7heresdk21VisualNavigatorColorsC03dayD0ACyFZ" class="token"><code>dayColors()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Retrieves HERE day color presets for route and maneuver arrow visualization.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func dayColors() -> VisualNavigatorColors
  ```

  </div>

  </div>

  <div>

  #### Return Value

  HERE day color presets for route and maneuver arrow visualization.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk21VisualNavigatorColorsC05nightD0ACyFZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-nightColors" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-visualnavigatorcolors#sdk-for-ios-navigate-s-7heresdk21VisualNavigatorColorsC05nightD0ACyFZ" class="token"><code>nightColors()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Retrieves HERE night color presets for route and maneuver arrow visualization.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func nightColors() -> VisualNavigatorColors
  ```

  </div>

  </div>

  <div>

  #### Return Value

  HERE night color presets for route and maneuver arrow visualization.

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

