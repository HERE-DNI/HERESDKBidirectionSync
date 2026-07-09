---
title: "VehicleProfileRestriction (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapdata-vehicleprofilerestriction"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-mapdata-package-summary">com.here.sdk.mapdata</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.mapdata.VehicleProfileRestriction → com.here.sdk.mapdata.VehicleProfileRestriction

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">VehicleProfileRestriction</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Physical and cargo profile of a vehicle that triggers a regulation. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

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

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-hazardousmaterialtype" title="enum class in com.here.sdk.mapdata">`HazardousMaterialType`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-vehicleprofilerestriction#hazardousMaterial" class="member-name-link"><code>hazardousMaterial</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Hazardous material condition associated with this profile.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-vehicletypecondition" title="enum class in com.here.sdk.mapdata">`VehicleTypeCondition`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-vehicleprofilerestriction#requestedVehicleType" class="member-name-link"><code>requestedVehicleType</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Vehicle type to which this restriction applies.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">`IntegerRange`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-vehicleprofilerestriction#requiredAmountOfTrailers" class="member-name-link"><code>requiredAmountOfTrailers</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Trailer count limits.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">`IntegerRange`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-vehicleprofilerestriction#requiredGrossWeightInKilograms" class="member-name-link"><code>requiredGrossWeightInKilograms</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Gross weight limits in kilograms.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">`IntegerRange`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-vehicleprofilerestriction#requiredWeightInKilograms" class="member-name-link"><code>requiredWeightInKilograms</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Weight limits in kilograms.

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

      VehicleProfileRestriction ( IntegerRange requiredWeightInKilograms, IntegerRange requiredGrossWeightInKilograms, IntegerRange requiredAmountOfTrailers, HazardousMaterialType hazardousMaterial)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance with specified parameters.

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

  - <div id="sdk-for-android-navigate-requestedVehicleType" class="section detail">

    ### requestedVehicleType

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-vehicletypecondition" title="enum class in com.here.sdk.mapdata">VehicleTypeCondition</a></span> <span class="element-name">requestedVehicleType</span>

    </div>

    <div class="block">

    Vehicle type to which this restriction applies.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-requiredWeightInKilograms" class="section detail">

    ### requiredWeightInKilograms

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a></span> <span class="element-name">requiredWeightInKilograms</span>

    </div>

    <div class="block">

    Weight limits in kilograms.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-requiredGrossWeightInKilograms" class="section detail">

    ### requiredGrossWeightInKilograms

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a></span> <span class="element-name">requiredGrossWeightInKilograms</span>

    </div>

    <div class="block">

    Gross weight limits in kilograms.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-requiredAmountOfTrailers" class="section detail">

    ### requiredAmountOfTrailers

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a></span> <span class="element-name">requiredAmountOfTrailers</span>

    </div>

    <div class="block">

    Trailer count limits.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-hazardousMaterial" class="section detail">

    ### hazardousMaterial

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-hazardousmaterialtype" title="enum class in com.here.sdk.mapdata">HazardousMaterialType</a></span> <span class="element-name">hazardousMaterial</span>

    </div>

    <div class="block">

    Hazardous material condition associated with this profile.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-com-here-sdk-core-IntegerRange-com-here-sdk-core-IntegerRange-com-here-sdk-core-IntegerRange-com-here-sdk-mapdata-HazardousMaterialType" class="section detail">

    ### VehicleProfileRestriction

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">VehicleProfileRestriction</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a> requiredWeightInKilograms, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a> requiredGrossWeightInKilograms, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a> requiredAmountOfTrailers, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapdata-hazardousmaterialtype" title="enum class in com.here.sdk.mapdata">HazardousMaterialType</a> hazardousMaterial)</span>

    </div>

    <div class="block">

    Creates a new instance with specified parameters.

    </div>

    Parameters:  
    `requiredWeightInKilograms` -

    Weight limits in kilograms.

    `requiredGrossWeightInKilograms` -

    Gross weight limits in kilograms.

    `requiredAmountOfTrailers` -

    Trailer count limits.

    `hazardousMaterial` -

    Hazardous material condition associated with this profile.

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

