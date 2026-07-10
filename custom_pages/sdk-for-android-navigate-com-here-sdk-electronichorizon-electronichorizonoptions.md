---
title: "ElectronicHorizonOptions (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonoptions"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-package-summary">com.here.sdk.electronichorizon</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.electronichorizon.ElectronicHorizonOptions → com.here.sdk.electronichorizon.ElectronicHorizonOptions

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">ElectronicHorizonOptions</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Provides options to configure ElectronicHorizonEngine . Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

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

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>`>`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonoptions#lookAheadDistancesInMeters" class="member-name-link"><code>lookAheadDistancesInMeters</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The ordered list of distances that define how far to look ahead in meters when calculating electronic horizon paths.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `double`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonoptions#trailingDistanceInMeters" class="member-name-link"><code>trailingDistanceInMeters</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The trailing distance of the electronic horizon path in meters.

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

      ElectronicHorizonOptions ( List < Double > lookAheadDistancesInMeters,
       double trailingDistanceInMeters)

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

  - <div id="sdk-for-android-navigate-lookAheadDistancesInMeters" class="section detail">

    ### lookAheadDistancesInMeters

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a>\></span> <span class="element-name">lookAheadDistancesInMeters</span>

    </div>

    <div class="block">

    The ordered list of distances that define how far to look ahead in meters when calculating electronic horizon paths. The first entry of the list is for the most preferred path, the second is for the side paths of the first level, the third is for the side paths of the second level, and so on. Each entry defines how far ahead the path should be provided. The valid number of values is from one to ten. Values beyond the tenth entry are removed from the list. If the list is empty, a single default distance value is used instead.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-trailingDistanceInMeters" class="section detail">

    ### trailingDistanceInMeters

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">trailingDistanceInMeters</span>

    </div>

    <div class="block">

    The trailing distance of the electronic horizon path in meters. Segments are removed from the path once they are passed and the distance to them exceeds this value.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-java-util-List-double" class="section detail">

    ### ElectronicHorizonOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">ElectronicHorizonOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a>\> lookAheadDistancesInMeters, double trailingDistanceInMeters)</span>

    </div>

    <div class="block">

    Creates a new instance. Offline availability: This property is available online and offline.

    </div>

    Parameters:  
    `lookAheadDistancesInMeters` -

    The ordered list of distances that define how far to look ahead in meters when calculating electronic horizon paths. The first entry of the list is for the most preferred path, the second is for the side paths of the first level, the third is for the side paths of the second level, and so on. Each entry defines how far ahead the path should be provided. The valid number of values is from one to ten. Values beyond the tenth entry are removed from the list. If the list is empty, a single default distance value is used instead.

    `trailingDistanceInMeters` -

    The trailing distance of the electronic horizon path in meters. Segments are removed from the path once they are passed and the distance to them exceeds this value.

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

