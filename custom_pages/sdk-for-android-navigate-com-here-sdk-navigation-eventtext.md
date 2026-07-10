---
title: "EventText (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-eventtext"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.navigation.EventText → com.here.sdk.navigation.EventText

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">EventText</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Contains all the information regarding the next text announcement.

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

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-eventtext#distanceInMeters" class="member-name-link"><code>distanceInMeters</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Distance in meters to the location of the event for which the text notification is given.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationdetails" title="class in com.here.sdk.navigation">`ManeuverNotificationDetails`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-eventtext#maneuverNotificationDetails" class="member-name-link"><code>maneuverNotificationDetails</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Information about the next maneuver.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-spatialnotificationdetails" title="class in com.here.sdk.navigation">`SpatialNotificationDetails`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-eventtext#spatialNotificationDetails" class="member-name-link"><code>spatialNotificationDetails</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Information for a spatial text notifications.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-eventtext#text" class="member-name-link"><code>text</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The text notification instruction.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-textnotificationtype" title="enum class in com.here.sdk.navigation">`TextNotificationType`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-eventtext#type" class="member-name-link"><code>type</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Indicates the type of text announcement

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

      EventText ( TextNotificationType type,
       double distanceInMeters, String text)

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

  - <div id="sdk-for-android-navigate-type" class="section detail">

    ### type

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-textnotificationtype" title="enum class in com.here.sdk.navigation">TextNotificationType</a></span> <span class="element-name">type</span>

    </div>

    <div class="block">

    Indicates the type of text announcement

    </div>

    </div>

  - <div id="sdk-for-android-navigate-distanceInMeters" class="section detail">

    ### distanceInMeters

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">distanceInMeters</span>

    </div>

    <div class="block">

    Distance in meters to the location of the event for which the text notification is given. Note: For greater distances, distance in kilometers is rounded to the nearest digit (0.5 or greater rounds up, else down) to simplify the distance phrase in ManeuverNotifications texts during navigation. Distance in miles is rounded to the nearest 0.5 step. For example, 3.5 kilometers are rounded to 4 kilometers and the notification will begin with After 4 kilometers... . However, 3.5 miles are not rounded up and the notification will begin with After three and a half miles... . Same for 3.7 miles, whereas 3.8 miles are rounded to 4 miles. Note that the measurement units itself are defined in the UnitSystem class.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-text" class="section detail">

    ### text

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">text</span>

    </div>

    <div class="block">

    The text notification instruction. The text is formatted and localized as specified via RouteTextOptions . Note: During navigation, the text will be always empty when the Maneuver is taken from the Navigator or VisualNavigator instance via the provided index. The text instruction that can be accessed from the Route instance is meant as preview and it is not necessarily matching the more comprehensive maneuver information you can access during navigation. This information can be enhanced with real-time ManeuverNotifications texts that can be used for spoken text notifications during a trip.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-maneuverNotificationDetails" class="section detail">

    ### maneuverNotificationDetails

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationdetails" title="class in com.here.sdk.navigation">ManeuverNotificationDetails</a></span> <span class="element-name">maneuverNotificationDetails</span>

    </div>

    <div class="block">

    Information about the next maneuver. Is non- null only for type equals to TextNotificationType.MANEUVER .

    </div>

    </div>

  - <div id="sdk-for-android-navigate-spatialNotificationDetails" class="section detail">

    ### spatialNotificationDetails

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-spatialnotificationdetails" title="class in com.here.sdk.navigation">SpatialNotificationDetails</a></span> <span class="element-name">spatialNotificationDetails</span>

    </div>

    <div class="block">

    Information for a spatial text notifications. When EventTextOptions.enableSpatialAudio is false, then this attribute will be null .

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-com-here-sdk-navigation-TextNotificationType-double-java-lang-String" class="section detail">

    ### EventText

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">EventText</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-textnotificationtype" title="enum class in com.here.sdk.navigation">TextNotificationType</a> type, double distanceInMeters, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> text)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `type` -

    Indicates the type of text announcement

    `distanceInMeters` -

    Distance in meters to the location of the event for which the text notification is given. **Note:** For greater distances, distance in kilometers is rounded to the nearest digit (0.5 or greater rounds up, else down) to simplify the distance phrase in `ManeuverNotifications` texts during navigation. Distance in miles is rounded to the nearest 0.5 step. For example, 3.5 kilometers are rounded to 4 kilometers and the notification will begin with `After 4 kilometers...`. However, 3.5 miles are not rounded up and the notification will begin with `After three and a half miles...`. Same for 3.7 miles, whereas 3.8 miles are rounded to 4 miles. Note that the measurement units itself are defined in the `UnitSystem` class.

    `text` -

    The text notification instruction. The text is formatted and localized as specified via <a href="sdk-for-android-navigate-com-here-sdk-routing-routetextoptions" title="class in com.here.sdk.routing">`RouteTextOptions`</a>. **Note:** During navigation, the text will be always empty when the <a href="sdk-for-android-navigate-com-here-sdk-routing-maneuver" title="class in com.here.sdk.routing">`Maneuver`</a> is taken from the `Navigator` or `VisualNavigator` instance via the provided index. The text instruction that can be accessed from the <a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing">`Route`</a> instance is meant as preview and it is not necessarily matching the more comprehensive maneuver information you can access during navigation. This information can be enhanced with real-time `ManeuverNotifications` texts that can be used for spoken text notifications during a trip.

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

