---
title: "IconProvider Class Reference"
slug: "sdk-for-ios-navigate-classes-iconprovider"
---

# IconProvider

<div class="declaration">

<div class="language">

``` highlight
public class IconProvider
```

</div>

</div>

This provider creates icons from a given set of parameters for map content and constraints for icon dimensions for a particular map scheme. The icon creation currently does not rely on map data. Therefore, it works without online connection.

<div class="aside aside-note">

Note

This feature is in BETA state and thus there can be bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

      init(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Initializes an icon provider instance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( _ mapContext : MapContext )
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
  <td><code> </code><em><code>mapContext</code></em><code> </code></td>
  <td><div>
  <p>The map context instance which is obtained using [MapView.mapContext].</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      createRoadShieldIcon(properties: mapScheme: assetType: widthConstraintInPixels: heightConstraintInPixels: callback: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an image displaying a road shield according to the given parameters.

  <div class="aside aside-note">

  Note

  This feature is in BETA state and thus there can be bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func createRoadShieldIcon ( properties : RoadShieldIconProperties , mapScheme : MapScheme , assetType : IconProviderAssetType , widthConstraintInPixels : UInt32 , heightConstraintInPixels : UInt32 , callback : @escaping IconProviderCallback )
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
  <td><code> </code><em><code>properties</code></em><code> </code></td>
  <td><div>
  <p>The properties which determine the kind of road shield to be created.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>mapScheme</code></em><code> </code></td>
  <td><div>
  <p>The map scheme for which the road shield should be created.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>assetType</code></em><code> </code></td>
  <td><div>
  <p>The asset type for which the road shield should be created.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>widthConstraintInPixels</code></em><code> </code></td>
  <td><div>
  <p>The maximum width of the road shield in pixels. The value is capped to a maximum of 4096 pixels. The image will be created as large as possible within the width and height constraints while maintaining the aspect ratio. If set to 0, the width will be calculated based on the heightConstraintInPixels to preserve the aspect ratio.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>heightConstraintInPixels</code></em><code> </code></td>
  <td><div>
  <p>The maximum height of the road shield in pixels. The value is capped to a maximum of 4096 pixels. The image will be created as large as possible within the width and height constraints while maintaining the aspect ratio. If set to 0, the original image-asset’s height will be used.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>callback</code></em><code> </code></td>
  <td><div>
  <p>The callback which is used to return the created image along with a description of the icon based on the type of road and/or place it is used, or an error code.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      createVehicleRestrictionIcon(pickingResult: mapScheme: assetType: sizeConstraintsInPixels: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an image representing a vehicle restriction as shown on the map, based on map content picking result.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func createVehicleRestrictionIcon ( pickingResult : PickMapContentResult . VehicleRestrictionResult , mapScheme : MapScheme , assetType : IconProviderAssetType , sizeConstraintsInPixels : Size2D , completion callback : @escaping IconProviderCallback )
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
  <td><code> </code><em><code>pickingResult</code></em><code> </code></td>
  <td><div>
  <p>The result of picking vehicle restrictions.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>mapScheme</code></em><code> </code></td>
  <td><div>
  <p>The map scheme for which the vehicle restriction icon should be created.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>assetType</code></em><code> </code></td>
  <td><div>
  <p>The asset type for which the vehicle restriction icon should be created.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>sizeConstraintsInPixels</code></em><code> </code></td>
  <td><div>
  <p>The maximum width and height of the icon in pixels. The values are capped to a maximum of 4096 pixels. The image will be created as large as possible within the width and height constraints while maintaining the aspect ratio. If either width or height is set to 0, it will be calculated automatically based on icon’s aspect ratio.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>callback</code></em><code> </code></td>
  <td><div>
  <p>The callback which is used to return the created image along with a description of the icon based on the type of road and/or place it is used, or an error code.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      createVehicleRestrictionIcon(properties: mapScheme: assetType: sizeConstraintsInPixels: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an image representing a vehicle restriction as shown on the map.

  In case when <a href="sdk-for-ios-navigate-structs-vehiclerestriction">`VehicleRestriction`</a> object specifies multiple types of restrictions, then the icon is generated for the first one according to the following priority: <a href="sdk-for-ios-navigate-structs-vehiclerestriction#/s:7heresdk18VehicleRestrictionV11restrictionAA08SpecificC0VSgvp">`VehicleRestriction.restriction`</a>, <a href="sdk-for-ios-navigate-structs-vehiclerestriction#/s:7heresdk18VehicleRestrictionV9axleCountAA12IntegerRangeVSgvp">`VehicleRestriction.axleCount`</a>, <a href="sdk-for-ios-navigate-structs-vehiclerestriction#/s:7heresdk18VehicleRestrictionV16axleCountInGroupAA12IntegerRangeVSgvp">`VehicleRestriction.axleCountInGroup`</a>, <a href="sdk-for-ios-navigate-structs-vehiclerestriction#/s:7heresdk18VehicleRestrictionV06hazmatC0AA017HazardousMaterialC0VSgvp">`VehicleRestriction.hazmatRestriction`</a>, <a href="sdk-for-ios-navigate-structs-vehiclerestriction#/s:7heresdk18VehicleRestrictionV12trailerCountAA12IntegerRangeVSgvp">`VehicleRestriction.trailerCount`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func createVehicleRestrictionIcon ( properties : VehicleRestrictionIconProperties , mapScheme : MapScheme , assetType : IconProviderAssetType , sizeConstraintsInPixels : Size2D , completion callback : @escaping IconProviderCallback )
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
  <td><code> </code><em><code>properties</code></em><code> </code></td>
  <td><div>
  <p>The properties of a restriction icon to be created.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>mapScheme</code></em><code> </code></td>
  <td><div>
  <p>The map scheme for which the vehicle restriction icon should be created.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>assetType</code></em><code> </code></td>
  <td><div>
  <p>The asset type for which the vehicle restriction icon should be created.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>sizeConstraintsInPixels</code></em><code> </code></td>
  <td><div>
  <p>The maximum width and height of the icon in pixels. The values are capped to a maximum of 4096 pixels. The image will be created as large as possible within the width and height constraints while maintaining the aspect ratio. If either width or height is set to 0, it will be calculated automatically based on icon’s aspect ratio.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>callback</code></em><code> </code></td>
  <td><div>
  <p>The callback which is used to return the created image along with a description of the icon based on the type of road and/or place it is used, or an error code.</p>
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

