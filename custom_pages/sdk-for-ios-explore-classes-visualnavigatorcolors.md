---
title: "VisualNavigatorColors Class Reference"
slug: "sdk-for-ios-explore-classes-visualnavigatorcolors"
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

This class contains colors used by <a href="sdk-for-ios-explore-classes-visualnavigator">`VisualNavigator`</a> to render the route and the maneuver arrow visualization.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk21VisualNavigatorColorsC18maneuverArrowColorSo7UIColorCvp"></span>` `<span id="//apple_ref/swift/Property/maneuverArrowColor" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-visualnavigatorcolors#/s:7heresdk21VisualNavigatorColorsC18maneuverArrowColorSo7UIColorCvp" class="token"><code>maneuverArrowColor</code></a>` `

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

  ` `<span id="/s:7heresdk21VisualNavigatorColorsC014trafficOnRouteD0AA07TrafficfgD0Vvp"></span>` `<span id="//apple_ref/swift/Property/trafficOnRouteColors" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-visualnavigatorcolors#/s:7heresdk21VisualNavigatorColorsC014trafficOnRouteD0AA07TrafficfgD0Vvp" class="token"><code>trafficOnRouteColors</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Colors used to visualize traffic conditions on the route ahead of the current location, for segments with a jam factor of 4.0 or higher. For route segments with a jam factor below 4.0 and those behind the current location, <a href="sdk-for-ios-explore-structs-routeprogresscolors">`RouteProgressColors`</a> are used instead.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var trafficOnRouteColors: TrafficOnRouteColors { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      setRouteProgressColors(sectionTransportMode: routeProgressColors: )

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
  public func setRouteProgressColors ( sectionTransportMode : SectionTransportMode , routeProgressColors : RouteProgressColors )
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

      getRouteProgressColors(sectionTransportMode: )

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
  public func getRouteProgressColors ( sectionTransportMode : SectionTransportMode ) -> RouteProgressColors
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

      dayColors()

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
  public static func dayColors () -> VisualNavigatorColors
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  HERE day color presets for route and maneuver arrow visualization.

  </div>

  </div>

  </div>

- <div>

      nightColors()

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
  public static func nightColors () -> VisualNavigatorColors
  ```

  </pre>

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

<div id="sdk-for-ios-explore-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

