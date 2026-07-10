---
title: "VehicleSpecificAccess (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapdata-vehiclespecificaccess"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-mapdata-package-summary">com.here.sdk.mapdata</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.mapdata.VehicleSpecificAccess → com.here.sdk.mapdata.VehicleSpecificAccess

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">VehicleSpecificAccess</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Access regulation for a specific vehicle type on a road segment. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

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

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-vehiclerestrictioncondition" title="class in com.here.sdk.mapdata">`VehicleRestrictionCondition`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-vehiclespecificaccess#condition" class="member-name-link"><code>condition</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Conditions under which this access regulation is active.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-vehiclespecificaccess#isPermitBased" class="member-name-link"><code>isPermitBased</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  If true, access is only permitted with a special permit.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-vehiclespecificaccess#noTruckInnermostLane" class="member-name-link"><code>noTruckInnermostLane</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  If true, trucks are prohibited from using the innermost lane.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-physicalstructure" title="enum class in com.here.sdk.mapdata">`PhysicalStructure`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-vehiclespecificaccess#physicalStructure" class="member-name-link"><code>physicalStructure</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Physical structure (e.g.

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

      VehicleSpecificAccess (boolean isPermitBased, PhysicalStructure physicalStructure, VehicleRestrictionCondition condition)

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

  - <div id="sdk-for-android-navigate-isPermitBased" class="section detail">

    ### isPermitBased

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isPermitBased</span>

    </div>

    <div class="block">

    If true, access is only permitted with a special permit.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-physicalStructure" class="section detail">

    ### physicalStructure

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-physicalstructure" title="enum class in com.here.sdk.mapdata">PhysicalStructure</a></span> <span class="element-name">physicalStructure</span>

    </div>

    <div class="block">

    Physical structure (e.g. bridge or tunnel) to which this access regulation applies.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-noTruckInnermostLane" class="section detail">

    ### noTruckInnermostLane

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a></span> <span class="element-name">noTruckInnermostLane</span>

    </div>

    <div class="block">

    If true, trucks are prohibited from using the innermost lane.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-condition" class="section detail">

    ### condition

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-vehiclerestrictioncondition" title="class in com.here.sdk.mapdata">VehicleRestrictionCondition</a></span> <span class="element-name">condition</span>

    </div>

    <div class="block">

    Conditions under which this access regulation is active.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-boolean-com-here-sdk-mapdata-PhysicalStructure-com-here-sdk-mapdata-VehicleRestrictionCondition" class="section detail">

    ### VehicleSpecificAccess

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">VehicleSpecificAccess</span><wbr></wbr><span class="parameters">(boolean isPermitBased, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapdata-physicalstructure" title="enum class in com.here.sdk.mapdata">PhysicalStructure</a> physicalStructure, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapdata-vehiclerestrictioncondition" title="class in com.here.sdk.mapdata">VehicleRestrictionCondition</a> condition)</span>

    </div>

    <div class="block">

    Creates a new instance with specified parameters.

    </div>

    Parameters:  
    `isPermitBased` -

    If true, access is only permitted with a special permit.

    `physicalStructure` -

    Physical structure (e.g. bridge or tunnel) to which this access regulation applies.

    `condition` -

    Conditions under which this access regulation is active.

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

