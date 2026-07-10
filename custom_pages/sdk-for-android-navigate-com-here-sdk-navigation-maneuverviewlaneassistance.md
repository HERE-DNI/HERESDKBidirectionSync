---
title: "ManeuverViewLaneAssistance (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-maneuverviewlaneassistance"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.navigation.ManeuverViewLaneAssistance → com.here.sdk.navigation.ManeuverViewLaneAssistance

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">ManeuverViewLaneAssistance</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

A class that provides lane assistance information for the next maneuver(s). During turn-by-turn navigation lane assistance can help a driver to choose the recommended lanes in order to complete the upcoming maneuvers. The notifications are synchronized with the EventTextListener . EventTextListener has 4 notification types for each maneuver: Range, Reminder, Distance and Action. Only the maneuver notification of type Distance will also notify a ManeuverViewLaneAssistance object (e.g. "After 400 meters, turn right onto Invalidenstraße"). The notification will not be sent when other types of maneuver notification are given. The notification will not be sent when no lane data is available. During tracking mode, no notifications are delivered. This ManeuverViewLaneAssistance information is valid until the next maneuver is reached.

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

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-navigation-lane" title="class in com.here.sdk.navigation">`Lane`</a>`>`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverviewlaneassistance#lanesForNextManeuver" class="member-name-link"><code>lanesForNextManeuver</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  A list of lanes on the current road that leads to the upcoming maneuver.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-navigation-lane" title="class in com.here.sdk.navigation">`Lane`</a>`>`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverviewlaneassistance#lanesForNextNextManeuver" class="member-name-link"><code>lanesForNextNextManeuver</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  A list of lanes on the road that leads to the maneuver after the upcoming maneuver.

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

      ManeuverViewLaneAssistance ( List < Lane > lanesForNextManeuver, List < Lane > lanesForNextNextManeuver)

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

  - <div id="sdk-for-android-navigate-lanesForNextManeuver" class="section detail">

    ### lanesForNextManeuver

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-navigation-lane" title="class in com.here.sdk.navigation">Lane</a>\></span> <span class="element-name">lanesForNextManeuver</span>

    </div>

    <div class="block">

    A list of lanes on the current road that leads to the upcoming maneuver. The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and the last index represents the rightmost lane. This is valid for both right-hand and left-hand driving countries. Contraflow lanes are not included in the list. The list is guaranteed to be non-empty. RoadAttributes.isRightDrivingSide indicates if this is a left-hand driving country or not.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-lanesForNextNextManeuver" class="section detail">

    ### lanesForNextNextManeuver

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-navigation-lane" title="class in com.here.sdk.navigation">Lane</a>\></span> <span class="element-name">lanesForNextNextManeuver</span>

    </div>

    <div class="block">

    A list of lanes on the road that leads to the maneuver after the upcoming maneuver. The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and the last index represents the rightmost lane. This is valid for both right-hand and left-hand driving countries. Contraflow lanes are not included in the list. RoadAttributes.isRightDrivingSide indicates if this is a left-hand driving country or not. By default, this list is empty. It will be filled when the next two maneuvers are too close to each other, or when the next two maneuvers are roundabout maneuvers. Note: This notification is delivered at the same time as the lanesForNextManeuver . There is no separate maneuver notification on the second maneuver when two maneuvers are are too close to each other.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-java-util-List-java-util-List" class="section detail">

    ### ManeuverViewLaneAssistance

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">ManeuverViewLaneAssistance</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-navigation-lane" title="class in com.here.sdk.navigation">Lane</a>\> lanesForNextManeuver, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-navigation-lane" title="class in com.here.sdk.navigation">Lane</a>\> lanesForNextNextManeuver)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `lanesForNextManeuver` -

    A list of lanes on the current road that leads to the upcoming maneuver. The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and the last index represents the rightmost lane. This is valid for both right-hand and left-hand driving countries. Contraflow lanes are not included in the list. The list is guaranteed to be non-empty. <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadattributes#isRightDrivingSide">`RoadAttributes.isRightDrivingSide`</a> indicates if this is a left-hand driving country or not.

    `lanesForNextNextManeuver` -

    A list of lanes on the road that leads to the maneuver after the upcoming maneuver. The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and the last index represents the rightmost lane. This is valid for both right-hand and left-hand driving countries. Contraflow lanes are not included in the list. <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadattributes#isRightDrivingSide">`RoadAttributes.isRightDrivingSide`</a> indicates if this is a left-hand driving country or not. By default, this list is empty. It will be filled when the next two maneuvers are too close to each other, or when the next two maneuvers are roundabout maneuvers. Note: This notification is delivered at the same time as the <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverviewlaneassistance#lanesForNextManeuver">`lanesForNextManeuver`</a>. There is no separate maneuver notification on the second maneuver when two maneuvers are are too close to each other.

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

