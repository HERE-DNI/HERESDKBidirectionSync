---
title: "MapSceneLights Class Reference"
slug: "sdk-for-ios-navigate-classes-mapscenelights"
---

# MapSceneLights

<div class="declaration">

<div class="language">

``` highlight
public class MapSceneLights
```

``` highlight
extension MapSceneLights: NativeBase
```

``` highlight
extension MapSceneLights: Hashable
```

</div>

</div>

Manage the lights and their attributes in a scene.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14MapSceneLightsC33AttributeSettingCompletionHandlera"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Alias-AttributeSettingCompletionHandler" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapscenelights#sdk-for-ios-navigate-s-7heresdk14MapSceneLightsC33AttributeSettingCompletionHandlera" class="token"><code>AttributeSettingCompletionHandler</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This callback function allows handling errors that occur during the setting of light attributes.

  Note: The error code `NO_LIGHTS` may be returned when attempting to set light attributes in map schemes that do not support lights, for instance `road.network` map scheme.

  Please refer to the error code documentation for further details on error handling.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias AttributeSettingCompletionHandler = (_ setLightError: MapSceneLights.AttributeSettingError?) -> Void
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mapscenelights-attributesettingerror">AttributeSettingError</a>

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
  <td><code> </code><em><code>setLightError</code></em><code> </code></td>
  <td><div>
  <p>The cause for the failure when setting the light attributes, or <code>nil</code> if no error occurred.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14MapSceneLightsC8CategoryO"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Enum-Category" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapscenelights#sdk-for-ios-navigate-s-7heresdk14MapSceneLightsC8CategoryO" class="token"><code>Category</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The scene uses three categories of lighting which are: Main light, Back light and Rim light. These lights are directional lights.

  The properties of all lights have an impact on the shading of 3D objects, for instance, extruded buildings within the scene. However, shadow casting is only affected by the direction of the main light.

  Category primarily serves as an identifier type for managing the lights.

  <a href="sdk-for-ios-navigate-classes-mapscenelights-category" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum Category : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14MapSceneLightsC21AttributeSettingErrorO"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Enum-AttributeSettingError" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapscenelights#sdk-for-ios-navigate-s-7heresdk14MapSceneLightsC21AttributeSettingErrorO" class="token"><code>AttributeSettingError</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Error enum indicating reasons for failure when setting light attributes.

  <a href="sdk-for-ios-navigate-classes-mapscenelights-attributesettingerror" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum AttributeSettingError : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14MapSceneLightsC9DirectionV"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Struct-Direction" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapscenelights#sdk-for-ios-navigate-s-7heresdk14MapSceneLightsC9DirectionV" class="token"><code>Direction</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The direction of lights as a pair of azimuth and altitude angles. See <https://en.wikipedia.org/wiki/Horizontal_coordinate_system>

  <a href="sdk-for-ios-navigate-classes-mapscenelights-direction" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct Direction : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14MapSceneLightsC8setColor8category5color10completionyAC8CategoryO_So7UIColorCyAC21AttributeSettingErrorOSgcSgtF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-setColor-category-color-completion" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapscenelights#sdk-for-ios-navigate-s-7heresdk14MapSceneLightsC8setColor8category5color10completionyAC8CategoryO_So7UIColorCyAC21AttributeSettingErrorOSgcSgtF" class="token"><code>setColor(category:</code><wbr></wbr><code>color:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Set a new color for the light based on its category.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setColor(category: MapSceneLights.Category, color: UIColor, completion: MapSceneLights.AttributeSettingCompletionHandler?)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mapscenelights-category">Category</a>
  - <a href="sdk-for-ios-navigate-classes-mapscenelights#sdk-for-ios-navigate-s-7heresdk14MapSceneLightsC33AttributeSettingCompletionHandlera">AttributeSettingCompletionHandler</a>

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
  <td><code> </code><em><code>category</code></em><code> </code></td>
  <td><div>
  <p>The category of light for which the color is set.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>color</code></em><code> </code></td>
  <td><div>
  <p>The Color type includes red, green, blue, and alpha components. The value of these components must be inside the range [0, 1].</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Optional callback that will receive the result of this operation.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14MapSceneLightsC12setIntensity8category9intensity10completionyAC8CategoryO_SdyAC21AttributeSettingErrorOSgcSgtF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-setIntensity-category-intensity-completion" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapscenelights#sdk-for-ios-navigate-s-7heresdk14MapSceneLightsC12setIntensity8category9intensity10completionyAC8CategoryO_SdyAC21AttributeSettingErrorOSgcSgtF" class="token"><code>setIntensity(category:</code><wbr></wbr><code>intensity:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Set a new intensity for the light based on its category.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setIntensity(category: MapSceneLights.Category, intensity: Double, completion: MapSceneLights.AttributeSettingCompletionHandler?)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mapscenelights-category">Category</a>
  - <a href="sdk-for-ios-navigate-classes-mapscenelights#sdk-for-ios-navigate-s-7heresdk14MapSceneLightsC33AttributeSettingCompletionHandlera">AttributeSettingCompletionHandler</a>

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
  <td><code> </code><em><code>category</code></em><code> </code></td>
  <td><div>
  <p>The category of light for which the intensity is set.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>intensity</code></em><code> </code></td>
  <td><div>
  <p>The light intensity value must be inside the range [0, 10]. The intensity value is clamped to this range. If the value falls outside its supported range, it will be adjusted to stay within the range. Note: When the intensity value is big, 3D objects might turn completely white because all the color channels could go over the limit of 1.0.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Optional callback that will receive the result of this operation.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14MapSceneLightsC12setDirection8category9direction10completionyAC8CategoryO_AC0F0VyAC21AttributeSettingErrorOSgcSgtF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-setDirection-category-direction-completion" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapscenelights#sdk-for-ios-navigate-s-7heresdk14MapSceneLightsC12setDirection8category9direction10completionyAC8CategoryO_AC0F0VyAC21AttributeSettingErrorOSgcSgtF" class="token"><code>setDirection(category:</code><wbr></wbr><code>direction:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Set a new direction for the light based on its category.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setDirection(category: MapSceneLights.Category, direction: MapSceneLights.Direction, completion: MapSceneLights.AttributeSettingCompletionHandler?)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mapscenelights-category">Category</a>
  - <a href="sdk-for-ios-navigate-classes-mapscenelights-direction">Direction</a>
  - <a href="sdk-for-ios-navigate-classes-mapscenelights#sdk-for-ios-navigate-s-7heresdk14MapSceneLightsC33AttributeSettingCompletionHandlera">AttributeSettingCompletionHandler</a>

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
  <td><code> </code><em><code>category</code></em><code> </code></td>
  <td><div>
  <p>The category of light for which the direction is set.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>direction</code></em><code> </code></td>
  <td><div>
  <p>The Direction contains azimuth and altitude angles in degrees.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Optional callback that will receive the result of this operation.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14MapSceneLightsC8getColor8categorySo7UIColorCSgAC8CategoryO_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-getColor-category" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapscenelights#sdk-for-ios-navigate-s-7heresdk14MapSceneLightsC8getColor8categorySo7UIColorCSgAC8CategoryO_tF" class="token"><code>getColor(category:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Retrieves the current color of the light based on its category.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getColor(category: MapSceneLights.Category) -> UIColor?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mapscenelights-category">Category</a>

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
  <td><code> </code><em><code>category</code></em><code> </code></td>
  <td><div>
  <p>The category of light from which the color is retrieved.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The current color of the light, or `nil` if the light is missing from the loaded scene or MapScene is not intitialized.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14MapSceneLightsC12getIntensity8categorySdSgAC8CategoryO_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-getIntensity-category" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapscenelights#sdk-for-ios-navigate-s-7heresdk14MapSceneLightsC12getIntensity8categorySdSgAC8CategoryO_tF" class="token"><code>getIntensity(category:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Retrieves the current intensity of the light based on its category.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getIntensity(category: MapSceneLights.Category) -> Double?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mapscenelights-category">Category</a>

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
  <td><code> </code><em><code>category</code></em><code> </code></td>
  <td><div>
  <p>The category of light from which the intensity is retrieved.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The current intensity of the light, or `nil` if the light is missing from the loaded scene or MapScene is not intitialized.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14MapSceneLightsC12getDirection8categoryAC0F0VSgAC8CategoryO_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-getDirection-category" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapscenelights#sdk-for-ios-navigate-s-7heresdk14MapSceneLightsC12getDirection8categoryAC0F0VSgAC8CategoryO_tF" class="token"><code>getDirection(category:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Retrieves the current direction of the light based on its category.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getDirection(category: MapSceneLights.Category) -> MapSceneLights.Direction?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mapscenelights-category">Category</a>
  - <a href="sdk-for-ios-navigate-classes-mapscenelights-direction">Direction</a>

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
  <td><code> </code><em><code>category</code></em><code> </code></td>
  <td><div>
  <p>The category of light from which the direction is retrieved.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The current direction of the light, or `nil` if the light is missing from the loaded scene or MapScene is not intitialized.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14MapSceneLightsC5resetyyF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-reset" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapscenelights#sdk-for-ios-navigate-s-7heresdk14MapSceneLightsC5resetyyF" class="token"><code>reset()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Resets all attributes of each light to their default values based on the current map scene settings.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func reset()
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

