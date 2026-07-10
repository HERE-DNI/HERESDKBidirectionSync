---
title: "IconProvider (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-iconprovider"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-mapview-package-summary">com.here.sdk.mapview</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.mapview.IconProvider → com.here.sdk.mapview.IconProvider

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public class </span><span class="element-name type-name-label">IconProvider</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

This provider creates icons from a given set of parameters for map content and constraints for icon dimensions for a particular map scheme. The icon creation currently does not rely on map data. Therefore, it works without online connection. Note: This feature is in BETA state and thus there can be bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

</div>

- <div id="sdk-for-android-navigate-nested-class-summary" class="section nested-class-summary">

  <div class="caption">

  Nested Classes

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Class

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  `static interface `

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-iconprovider-iconcallback" class="type-name-link" title="interface in com.here.sdk.mapview"><code>IconProvider.IconCallback</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Interface which is used as callback to pass back an image or error code after calling the createRoadShieldIcon() method.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-summary" class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Constructor

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-constructor-name even-row-color">

      IconProvider ( MapContext mapContext)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates an IconProvider.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-method-summary" class="section method-summary">

  <div id="sdk-for-android-navigate-method-summary-table">

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Method

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      createRoadShieldIcon ( RoadShieldIconProperties properties, MapScheme mapScheme, IconProviderAssetType assetType,
       long widthConstraintInPixels,
       long heightConstraintInPixels, IconProvider.IconCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Creates an image displaying a road shield according to the given parameters.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      createVehicleRestrictionIcon ( PickMapContentResult.VehicleRestrictionResult pickingResult, MapScheme mapScheme, IconProviderAssetType assetType, Size2D sizeConstraintsInPixels, IconProvider.IconCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Creates an image representing a vehicle restriction as shown on the map, based on map content picking result.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      createVehicleRestrictionIcon ( VehicleRestrictionIconProperties iconProperties, MapScheme mapScheme, IconProviderAssetType assetType, Size2D sizeConstraintsInPixels, IconProvider.IconCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Creates an image representing a vehicle restriction as shown on the map.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-com-here-sdk-mapview-MapContext" class="section detail">

    ### IconProvider

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">IconProvider</span><wbr></wbr><span class="parameters">(<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontext" title="class in com.here.sdk.mapview">MapContext</a> mapContext)</span>

    </div>

    <div class="block">

    Creates an IconProvider.

    </div>

    Parameters:  
    `mapContext` - The map context instance.

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-createRoadShieldIcon-com-here-sdk-mapview-RoadShieldIconProperties-com-here-sdk-mapview-MapScheme-com-here-sdk-mapview-IconProviderAssetType-long-long-com-here-sdk-mapview-IconProvider-IconCallback" class="section detail">

    ### createRoadShieldIcon

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">createRoadShieldIcon</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-roadshieldiconproperties" title="class in com.here.sdk.mapview">RoadShieldIconProperties</a> properties, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscheme" title="enum class in com.here.sdk.mapview">MapScheme</a> mapScheme, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-iconproviderassettype" title="enum class in com.here.sdk.mapview">IconProviderAssetType</a> assetType, long widthConstraintInPixels, long heightConstraintInPixels, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-iconprovider-iconcallback" title="interface in com.here.sdk.mapview">IconProvider.IconCallback</a> callback)</span>

    </div>

    <div class="block">

    Creates an image displaying a road shield according to the given parameters.

    </div>

    Parameters:  
    `properties` - The properties which determine the kind of road shield to be created.

    `mapScheme` - The map scheme for which the road shield should be created.

    `assetType` - The asset type for which the road shield should be created.

    `widthConstraintInPixels` - The maximum width of the road shield in pixels. The value is capped to a maximum of 4096 pixels. The image will be created as large as possible within the width and height constraints while maintaining the aspect ratio. If set to 0, the width will be calculated based on the heightConstraintInPixels to preserve the aspect ratio.

    `heightConstraintInPixels` - The maximum height of the road shield in pixels. The value is capped to a maximum of 4096 pixels. The image will be created as large as possible within the width and height constraints while maintaining the aspect ratio. If set to 0, the original image-asset's height will be used.

    `callback` - The callback which is used to return the created image or an error code. Note: This feature is in BETA state and thus there can be bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

    </div>

  - <div id="sdk-for-android-navigate-createVehicleRestrictionIcon-com-here-sdk-mapview-PickMapContentResult-VehicleRestrictionResult-com-here-sdk-mapview-MapScheme-com-here-sdk-mapview-IconProviderAssetType-com-here-sdk-core-Size2D-com-here-sdk-mapview-IconProvider-IconCallback" class="section detail">

    ### createVehicleRestrictionIcon

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">createVehicleRestrictionIcon</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-pickmapcontentresult-vehiclerestrictionresult" title="class in com.here.sdk.mapview">PickMapContentResult.VehicleRestrictionResult</a> pickingResult, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscheme" title="enum class in com.here.sdk.mapview">MapScheme</a> mapScheme, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-iconproviderassettype" title="enum class in com.here.sdk.mapview">IconProviderAssetType</a> assetType, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-size2d" title="class in com.here.sdk.core">Size2D</a> sizeConstraintsInPixels, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-iconprovider-iconcallback" title="interface in com.here.sdk.mapview">IconProvider.IconCallback</a> callback)</span>

    </div>

    <div class="block">

    Creates an image representing a vehicle restriction as shown on the map, based on map content picking result.

    </div>

    Parameters:  
    `pickingResult` - The result of picking vehicle restrictions.

    `mapScheme` - The map scheme for which the vehicle restriction icon should be created.

    `assetType` - The asset type for which the vehicle restriction icon should be created.

    `sizeConstraintsInPixels` - The maximum width and height of the icon in pixels. The values are capped to a maximum of 4096 pixels. The image will be created as large as possible within the width and height constraints while maintaining the aspect ratio. If either width or height is set to 0, it will be calculated automatically based on icon's aspect ratio.

    `callback` - The callback which is used to return the created image, or an error code.

    </div>

  - <div id="sdk-for-android-navigate-createVehicleRestrictionIcon-com-here-sdk-mapview-VehicleRestrictionIconProperties-com-here-sdk-mapview-MapScheme-com-here-sdk-mapview-IconProviderAssetType-com-here-sdk-core-Size2D-com-here-sdk-mapview-IconProvider-IconCallback" class="section detail">

    ### createVehicleRestrictionIcon

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">createVehicleRestrictionIcon</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-vehiclerestrictioniconproperties" title="class in com.here.sdk.mapview">VehicleRestrictionIconProperties</a> iconProperties, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscheme" title="enum class in com.here.sdk.mapview">MapScheme</a> mapScheme, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-iconproviderassettype" title="enum class in com.here.sdk.mapview">IconProviderAssetType</a> assetType, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-size2d" title="class in com.here.sdk.core">Size2D</a> sizeConstraintsInPixels, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-iconprovider-iconcallback" title="interface in com.here.sdk.mapview">IconProvider.IconCallback</a> callback)</span>

    </div>

    <div class="block">

    Creates an image representing a vehicle restriction as shown on the map. In case when \`VehicleRestriction\` object specifies multiple types of restrictions, then the icon is generated for the first one according to the following priority: VehicleRestriction.restriction , VehicleRestriction.axleCount , VehicleRestriction.axleCountInGroup , VehicleRestriction.hazmatRestriction , VehicleRestriction.trailerCount .

    </div>

    Parameters:  
    `iconProperties` - The properties of the icon.

    `mapScheme` - The map scheme for which the vehicle restriction icon should be created.

    `assetType` - The asset type for which the vehicle restriction icon should be created.

    `sizeConstraintsInPixels` - The maximum width and height of the icon in pixels. The values are capped to a maximum of 4096 pixels. The image will be created as large as possible within the width and height constraints while maintaining the aspect ratio. If either width or height is set to 0, it will be calculated automatically based on icon's aspect ratio.

    `callback` - The callback which is used to return the created image, or an error code.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

