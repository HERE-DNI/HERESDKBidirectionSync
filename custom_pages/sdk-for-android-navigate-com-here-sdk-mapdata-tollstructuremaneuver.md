---
title: "TollStructureManeuver (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapdata-tollstructuremaneuver"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-mapdata-package-summary">com.here.sdk.mapdata</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.mapdata.TollStructureManeuver → com.here.sdk.mapdata.TollStructureManeuver

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">TollStructureManeuver</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

A class that provides information for a toll structure at a toll point.

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

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-mapdata-directedocmsegmentid" title="class in com.here.sdk.mapdata">`DirectedOCMSegmentId`</a>`>`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-tollstructuremaneuver#destinations" class="member-name-link"><code>destinations</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Optional destinations segment references.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-filereference" title="class in com.here.sdk.mapdata">`FileReference`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-tollstructuremaneuver#etcGuidanceFile" class="member-name-link"><code>etcGuidanceFile</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Optional image providing guidance through an electronic toll collection (ETC) point.

  </div>

  </div>

  <div class="col-first even-row-color">

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-tollstructuremaneuver#isCheckpoint" class="member-name-link"><code>isCheckpoint</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Vehicle Checkpoint identifies locations on the through route, where vehicles are required to slow down/stop with the intended purpose of inspecting vehicles to deter illegal immigration and smuggling activities, to perform customs/passport checks, toll payment, etc.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-tollstructure" title="class in com.here.sdk.mapdata">`TollStructure`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-tollstructuremaneuver#tollStructure" class="member-name-link"><code>tollStructure</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Toll structure properties Could be empty for checkpoint not related to toll.

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

      TollStructureManeuver ( List < DirectedOCMSegmentId > destinations)

  </div>

  <div class="col-last even-row-color">

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

  - <div id="sdk-for-android-navigate-tollStructure" class="section detail">

    ### tollStructure

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-tollstructure" title="class in com.here.sdk.mapdata">TollStructure</a></span> <span class="element-name">tollStructure</span>

    </div>

    <div class="block">

    Toll structure properties Could be empty for checkpoint not related to toll.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-isCheckpoint" class="section detail">

    ### isCheckpoint

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isCheckpoint</span>

    </div>

    <div class="block">

    Vehicle Checkpoint identifies locations on the through route, where vehicles are required to slow down/stop with the intended purpose of inspecting vehicles to deter illegal immigration and smuggling activities, to perform customs/passport checks, toll payment, etc. This is not limited to border locations.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-destinations" class="section detail">

    ### destinations

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-mapdata-directedocmsegmentid" title="class in com.here.sdk.mapdata">DirectedOCMSegmentId</a>\></span> <span class="element-name">destinations</span>

    </div>

    <div class="block">

    Optional destinations segment references. Destination shows for which exactly outgoing segment current toll/checkpoint is applied. Empty if structure applied to all outgoing connected segments.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-etcGuidanceFile" class="section detail">

    ### etcGuidanceFile

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-filereference" title="class in com.here.sdk.mapdata">FileReference</a></span> <span class="element-name">etcGuidanceFile</span>

    </div>

    <div class="block">

    Optional image providing guidance through an electronic toll collection (ETC) point.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-java-util-List" class="section detail">

    ### TollStructureManeuver

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">TollStructureManeuver</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-mapdata-directedocmsegmentid" title="class in com.here.sdk.mapdata">DirectedOCMSegmentId</a>\> destinations)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `destinations` -

    Optional destinations segment references. Destination shows for which exactly outgoing segment current toll/checkpoint is applied. Empty if structure applied to all outgoing connected segments.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

