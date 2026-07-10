---
title: "TMCData (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcdata"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-package-summary">com.here.sdk.trafficbroadcast</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.trafficbroadcast.TMCData → com.here.sdk.trafficbroadcast.TMCData

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">TMCData</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Represents the traffic events in RDS-TMC format.

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

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang"><code>Integer</code></a>`>`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcdata#additionalEvents" class="member-name-link"><code>additionalEvents</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Additional traffic events.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" class="external-link" title="class or interface in java.lang"><code>Long</code></a>`>`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcdata#additionalLocations" class="member-name-link"><code>additionalLocations</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Additional traffic locations.

  </div>

  </div>

  <div class="col-first even-row-color">

  `short`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcdata#direction" class="member-name-link"><code>direction</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Street direction.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `short`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcdata#diversionAdvice" class="member-name-link"><code>diversionAdvice</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Diversion advice.

  </div>

  </div>

  <div class="col-first even-row-color">

  `short`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcdata#durationPersistence" class="member-name-link"><code>durationPersistence</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Duration persitence.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `int`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcdata#event" class="member-name-link"><code>event</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Traffic event data.

  </div>

  </div>

  <div class="col-first even-row-color">

  `short`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcdata#extent" class="member-name-link"><code>extent</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Extent.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `long`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcdata#location" class="member-name-link"><code>location</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Traffic event location.

  </div>

  </div>

  <div class="col-first even-row-color">

  `short`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcdata#numberOfGroups" class="member-name-link"><code>numberOfGroups</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Number of groups (1 to 5).

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

      TMCData (short numberOfGroups,
       short extent,
       short direction,
       short diversionAdvice,
       short durationPersistence,
       int event,
       long location, List < Integer > additionalEvents, List < Long > additionalLocations)

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

  - <div id="sdk-for-android-navigate-numberOfGroups" class="section detail">

    ### numberOfGroups

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">short</span> <span class="element-name">numberOfGroups</span>

    </div>

    <div class="block">

    Number of groups (1 to 5).

    </div>

    </div>

  - <div id="sdk-for-android-navigate-extent" class="section detail">

    ### extent

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">short</span> <span class="element-name">extent</span>

    </div>

    <div class="block">

    Extent.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-direction" class="section detail">

    ### direction

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">short</span> <span class="element-name">direction</span>

    </div>

    <div class="block">

    Street direction.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-diversionAdvice" class="section detail">

    ### diversionAdvice

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">short</span> <span class="element-name">diversionAdvice</span>

    </div>

    <div class="block">

    Diversion advice.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-durationPersistence" class="section detail">

    ### durationPersistence

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">short</span> <span class="element-name">durationPersistence</span>

    </div>

    <div class="block">

    Duration persitence.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-event" class="section detail">

    ### event

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">event</span>

    </div>

    <div class="block">

    Traffic event data.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-location" class="section detail">

    ### location

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">location</span>

    </div>

    <div class="block">

    Traffic event location.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-additionalEvents" class="section detail">

    ### additionalEvents

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a>\></span> <span class="element-name">additionalEvents</span>

    </div>

    <div class="block">

    Additional traffic events.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-additionalLocations" class="section detail">

    ### additionalLocations

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" class="external-link" title="class or interface in java.lang">Long</a>\></span> <span class="element-name">additionalLocations</span>

    </div>

    <div class="block">

    Additional traffic locations.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-short-short-short-short-short-int-long-java-util-List-java-util-List" class="section detail">

    ### TMCData

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">TMCData</span><wbr></wbr><span class="parameters">(short numberOfGroups, short extent, short direction, short diversionAdvice, short durationPersistence, int event, long location, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a>\> additionalEvents, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" class="external-link" title="class or interface in java.lang">Long</a>\> additionalLocations)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `numberOfGroups` -

    Number of groups (1 to 5).

    `extent` -

    Extent.

    `direction` -

    Street direction.

    `diversionAdvice` -

    Diversion advice.

    `durationPersistence` -

    Duration persitence.

    `event` -

    Traffic event data.

    `location` -

    Traffic event location.

    `additionalEvents` -

    Additional traffic events.

    `additionalLocations` -

    Additional traffic locations.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

