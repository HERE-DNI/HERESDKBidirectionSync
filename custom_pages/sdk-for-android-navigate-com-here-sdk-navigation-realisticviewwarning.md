---
title: "RealisticViewWarning (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarning"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.navigation.RealisticViewWarning → com.here.sdk.navigation.RealisticViewWarning

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">RealisticViewWarning</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

A realistic view notification. This notification is given for complex junctions and it includes a visual representation of that junction, in order to help the user to better navigate it. When distanceType is DistanceType.AHEAD , the realisticViewVectorImage object will be provided with the junction view and the signpost representations. For distanceType with value DistanceType.PASSED , the realisticViewVectorImage object will be null. Use RealisticViewWarningListener to get notifications about the realistic views of the upcoming junctions. Realistic view notifications require an online connection in order to function properly, or that the junction or signpost map layer data is cached, installed or preloaded as part of a Region . This can be enabled via feature configurations.

</div>

</div>

- <div id="sdk-for-android-navigate-field-summary" class="section field-summary">

  <div class="caption">

  Fields

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Field

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  `double`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarning#distanceToRealisticViewInMeters" class="member-name-link"><code>distanceToRealisticViewInMeters</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Distance to the junction, for which the realistic view is given, expressed in meters.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-distancetype" title="enum class in com.here.sdk.navigation">`DistanceType`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarning#distanceType" class="member-name-link"><code>distanceType</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The distance type for the warning, e.g.

  </div>

  </div>

  <div class="col-first even-row-color">

  `int`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarning#id" class="member-name-link"><code>id</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Unique identifier for this specific realistic view warning instance.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewrasterimage" title="class in com.here.sdk.navigation">`RealisticViewRasterImage`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarning#realisticViewRasterImage" class="member-name-link"><code>realisticViewRasterImage</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The realistic view object for which the warning is given.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewvectorimage" title="class in com.here.sdk.navigation">`RealisticViewVectorImage`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarning#realisticViewVectorImage" class="member-name-link"><code>realisticViewVectorImage</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The realistic view object for which the warning is given.

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

      RealisticViewWarning (double distanceToRealisticViewInMeters, DistanceType distanceType)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

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

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      equals ( Object obj)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      hashCode ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-field-detail" class="section field-details">

  - <div id="sdk-for-android-navigate-id" class="section detail">

    ### id

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">id</span>

    </div>

    <div class="block">

    Unique identifier for this specific realistic view warning instance. Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace. Use this ID to track, update, or dismiss individual warning instances of this type.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-distanceToRealisticViewInMeters" class="section detail">

    ### distanceToRealisticViewInMeters

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">distanceToRealisticViewInMeters</span>

    </div>

    <div class="block">

    Distance to the junction, for which the realistic view is given, expressed in meters.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-realisticViewVectorImage" class="section detail">

    ### realisticViewVectorImage

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewvectorimage" title="class in com.here.sdk.navigation">RealisticViewVectorImage</a></span> <span class="element-name">realisticViewVectorImage</span>

    </div>

    <div class="block">

    The realistic view object for which the warning is given. Image resources are stored as vector graphics. Within RealisticViewWarning , only one type of image, either raster or vector, will be provided. If this property is not null , then realisticViewRasterImage will be null . Note: The realistic views for most of the countries are stored as vector images.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-realisticViewRasterImage" class="section detail">

    ### realisticViewRasterImage

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewrasterimage" title="class in com.here.sdk.navigation">RealisticViewRasterImage</a></span> <span class="element-name">realisticViewRasterImage</span>

    </div>

    <div class="block">

    The realistic view object for which the warning is given. Image resources are stored as raster graphics. Within RealisticViewWarning , only one type of image, either raster or vector, will be provided. If this property is not null , then realisticViewVectorImage will be null . Note: Certain countries support only raster images as realistic views. Currently, this is the case only for Japan, but in the future, more countries might support this type of realistic views.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-distanceType" class="section detail">

    ### distanceType

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a></span> <span class="element-name">distanceType</span>

    </div>

    <div class="block">

    The distance type for the warning, e.g. a warning for a new realistic view ahead or a warning for passing a realistic view. Since the realistic view warning is given relative to a single position on the route, DistanceType.REACHED will never be given for this warning.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-double-com-here-sdk-navigation-DistanceType" class="section detail">

    ### RealisticViewWarning

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RealisticViewWarning</span><wbr></wbr><span class="parameters">(double distanceToRealisticViewInMeters, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a> distanceType)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `distanceToRealisticViewInMeters` -

    Distance to the junction, for which the realistic view is given, expressed in meters.

    `distanceType` -

    The distance type for the warning, e.g. a warning for a new realistic view ahead or a warning for passing a realistic view. Since the realistic view warning is given relative to a single position on the route, <a href="sdk-for-android-navigate-com-here-sdk-navigation-distancetype#REACHED">`DistanceType.REACHED`</a> will never be given for this warning.

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-equals-java-lang-Object" class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr></wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-navigate-hashCode" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

