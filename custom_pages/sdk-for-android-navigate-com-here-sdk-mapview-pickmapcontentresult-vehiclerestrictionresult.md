---
title: "PickMapContentResult.VehicleRestrictionResult (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-pickmapcontentresult-vehiclerestrictionresult"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-mapview-package-summary">com.here.sdk.mapview</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.mapview.PickMapContentResult.VehicleRestrictionResult → com.here.sdk.mapview.PickMapContentResult.VehicleRestrictionResult

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

Enclosing class:  
<a href="sdk-for-android-navigate-com-here-sdk-mapview-pickmapcontentresult" title="class in com.here.sdk.mapview">PickMapContentResult</a>

<div class="type-signature">

<span class="modifiers">public static final class </span><span class="element-name type-name-label">PickMapContentResult.VehicleRestrictionResult</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Carries the result of picking a vehicle restriction object.

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

  <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">`GeoCoordinates`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-pickmapcontentresult-vehiclerestrictionresult#coordinates" class="member-name-link"><code>coordinates</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The geographic coordinates of the vehicle restriction.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-core-countrycode" title="enum class in com.here.sdk.core">`CountryCode`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-pickmapcontentresult-vehiclerestrictionresult#countryCode" class="member-name-link"><code>countryCode</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Country code.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-transport-vehiclerestriction" title="class in com.here.sdk.transport">`VehicleRestriction`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-pickmapcontentresult-vehiclerestrictionresult#vehicleRestriction" class="member-name-link"><code>vehicleRestriction</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The vehicle restriction details.

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

      VehicleRestrictionResult ( GeoCoordinates coordinates, CountryCode countryCode, VehicleRestriction vehicleRestriction)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      VehicleRestrictionResult ( GeoCoordinates coordinates, VehicleRestriction vehicleRestriction)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-method-summary" class="section method-summary">

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-field-detail" class="section field-details">

  - <div id="sdk-for-android-navigate-coordinates" class="section detail">

    ### coordinates

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span class="element-name">coordinates</span>

    </div>

    <div class="block">

    The geographic coordinates of the vehicle restriction.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-countryCode" class="section detail">

    ### countryCode

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-countrycode" title="enum class in com.here.sdk.core">CountryCode</a></span> <span class="element-name">countryCode</span>

    </div>

    <div class="block">

    Country code.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-vehicleRestriction" class="section detail">

    ### vehicleRestriction

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-transport-vehiclerestriction" title="class in com.here.sdk.transport">VehicleRestriction</a></span> <span class="element-name">vehicleRestriction</span>

    </div>

    <div class="block">

    The vehicle restriction details.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-com-here-sdk-core-GeoCoordinates-com-here-sdk-transport-VehicleRestriction" class="section detail">

    ### VehicleRestrictionResult

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">VehicleRestrictionResult</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-transport-vehiclerestriction" title="class in com.here.sdk.transport">VehicleRestriction</a> vehicleRestriction)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `coordinates` -

    The geographic coordinates of the vehicle restriction.

    `vehicleRestriction` -

    The vehicle restriction details.

    </div>

  - <div id="sdk-for-android-navigate-init-com-here-sdk-core-GeoCoordinates-com-here-sdk-core-CountryCode-com-here-sdk-transport-VehicleRestriction" class="section detail">

    ### VehicleRestrictionResult

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">VehicleRestrictionResult</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates, @Nullable <a href="sdk-for-android-navigate-com-here-sdk-core-countrycode" title="enum class in com.here.sdk.core">CountryCode</a> countryCode, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-transport-vehiclerestriction" title="class in com.here.sdk.transport">VehicleRestriction</a> vehicleRestriction)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `coordinates` -

    The geographic coordinates of the vehicle restriction.

    `countryCode` -

    Country code.

    `vehicleRestriction` -

    The vehicle restriction details.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

