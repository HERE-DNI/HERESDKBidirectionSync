---
title: "TrackingCameraBehavior.ManeuverRule (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuverrule"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.navigation.TrackingCameraBehavior.ManeuverRule → com.here.sdk.navigation.TrackingCameraBehavior.ManeuverRule

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

Enclosing class:  
<a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior" title="class in com.here.sdk.navigation">TrackingCameraBehavior</a>

<div class="type-signature">

<span class="modifiers">public static final class </span><span class="element-name type-name-label">TrackingCameraBehavior.ManeuverRule</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Defines a single rule that determines how TrackingCameraBehavior reacts to nearby maneuvers when the current position matches this rule.

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

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-routing-functionalroadclass" title="enum class in com.here.sdk.routing">`FunctionalRoadClass`</a>`>`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuverrule#functionalRoadClasses" class="member-name-link"><code>functionalRoadClasses</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  List of functional road classes for which this rule applies.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-routing-maneuveraction" title="enum class in com.here.sdk.routing">`ManeuverAction`</a>`>`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuverrule#maneuverActions" class="member-name-link"><code>maneuverActions</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  List of maneuver actions for which this rule applies.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuverruleoptions" title="class in com.here.sdk.navigation">`TrackingCameraBehavior.ManeuverRuleOptions`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuverrule#maneuverRuleOptions" class="member-name-link"><code>maneuverRuleOptions</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The options for this rule.

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

      ManeuverRule ()

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

  - <div id="sdk-for-android-navigate-functionalRoadClasses" class="section detail">

    ### functionalRoadClasses

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-routing-functionalroadclass" title="enum class in com.here.sdk.routing">FunctionalRoadClass</a>\></span> <span class="element-name">functionalRoadClasses</span>

    </div>

    <div class="block">

    List of functional road classes for which this rule applies. The list is unordered. When empty, this rule applies to all functional road classes. Defaults to an empty list.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-maneuverActions" class="section detail">

    ### maneuverActions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-routing-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a>\></span> <span class="element-name">maneuverActions</span>

    </div>

    <div class="block">

    List of maneuver actions for which this rule applies. The list is unordered. When empty, this rule applies to all maneuver actions. Defaults to an empty list.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-maneuverRuleOptions" class="section detail">

    ### maneuverRuleOptions

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuverruleoptions" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ManeuverRuleOptions</a></span> <span class="element-name">maneuverRuleOptions</span>

    </div>

    <div class="block">

    The options for this rule. When set to null , the camera does not react to maneuvers that match this rule. Defaults to null .

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init" class="section detail">

    ### ManeuverRule

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">ManeuverRule</span>()

    </div>

    <div class="block">

    Creates a new instance. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    </div>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

