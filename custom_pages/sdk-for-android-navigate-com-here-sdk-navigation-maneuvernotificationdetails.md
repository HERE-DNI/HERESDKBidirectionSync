---
title: "ManeuverNotificationDetails (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationdetails"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.navigation.ManeuverNotificationDetails → com.here.sdk.navigation.ManeuverNotificationDetails

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">ManeuverNotificationDetails</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

This class provides the information regarding the next maneuver to be triggered

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

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationdetails#isCombinedManeuverText" class="member-name-link"><code>isCombinedManeuverText</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Indicates whether the current text notification combines information regarding current and next maneuver, such as, "Now turn right and then turn left onto Invalidenstrasse", or not.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-maneuver" title="class in com.here.sdk.routing">`Maneuver`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationdetails#maneuver" class="member-name-link"><code>maneuver</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Current maneuver data.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtype" title="enum class in com.here.sdk.navigation">`ManeuverNotificationType`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationdetails#maneuverNotificationType" class="member-name-link"><code>maneuverNotificationType</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Indicates the type of the current maneuver notification.

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

      ManeuverNotificationDetails ( Maneuver maneuver, ManeuverNotificationType maneuverNotificationType)

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

  - <div id="sdk-for-android-navigate-maneuver" class="section detail">

    ### maneuver

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-maneuver" title="class in com.here.sdk.routing">Maneuver</a></span> <span class="element-name">maneuver</span>

    </div>

    <div class="block">

    Current maneuver data. In case of a double maneuver e.g. "Now turn right and then turn left", this attribute will contain the maneuver data of the first maneuver of the combined maneuver "Now turn right".

    </div>

    </div>

  - <div id="sdk-for-android-navigate-maneuverNotificationType" class="section detail">

    ### maneuverNotificationType

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtype" title="enum class in com.here.sdk.navigation">ManeuverNotificationType</a></span> <span class="element-name">maneuverNotificationType</span>

    </div>

    <div class="block">

    Indicates the type of the current maneuver notification.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-isCombinedManeuverText" class="section detail">

    ### isCombinedManeuverText

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isCombinedManeuverText</span>

    </div>

    <div class="block">

    Indicates whether the current text notification combines information regarding current and next maneuver, such as, "Now turn right and then turn left onto Invalidenstrasse", or not.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-com-here-sdk-routing-Maneuver-com-here-sdk-navigation-ManeuverNotificationType" class="section detail">

    ### ManeuverNotificationDetails

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">ManeuverNotificationDetails</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-maneuver" title="class in com.here.sdk.routing">Maneuver</a> maneuver, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtype" title="enum class in com.here.sdk.navigation">ManeuverNotificationType</a> maneuverNotificationType)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `maneuver` -

    Current maneuver data. In case of a double maneuver e.g. "Now turn right and then turn left", this attribute will contain the maneuver data of the first maneuver of the combined maneuver "Now turn right".

    `maneuverNotificationType` -

    Indicates the type of the current maneuver notification.

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

