---
title: "CurrentSituationLaneView (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-currentsituationlaneview"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.navigation.CurrentSituationLaneView → com.here.sdk.navigation.CurrentSituationLaneView

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">CurrentSituationLaneView</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

A class that provides current situation lane assistance view information for the street at the current position of a single lane. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

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

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess" title="class in com.here.sdk.navigation">`LaneAccess`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-currentsituationlaneview#access" class="member-name-link"><code>access</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Indicates which vehicle types can access this lane.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-lanedirectioncategory" title="class in com.here.sdk.navigation">`LaneDirectionCategory`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-currentsituationlaneview#directionCategory" class="member-name-link"><code>directionCategory</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Indicates towards which directions this lane leads.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-navigation-lanedirection" title="enum class in com.here.sdk.navigation">`LaneDirection`</a>`>`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-currentsituationlaneview#directions" class="member-name-link"><code>directions</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Indicates which lane directions are available for this lane.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-navigation-lanedirection" title="enum class in com.here.sdk.navigation">`LaneDirection`</a>`>`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-currentsituationlaneview#directionsOnRoute" class="member-name-link"><code>directionsOnRoute</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Indicates which lane directions are on the route.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-lanemarkings" title="class in com.here.sdk.navigation">`LaneMarkings`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-currentsituationlaneview#laneMarkings" class="member-name-link"><code>laneMarkings</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Indicates the lane markings between the lanes.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-lanetype" title="class in com.here.sdk.navigation">`LaneType`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-currentsituationlaneview#type" class="member-name-link"><code>type</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Indicates this lane's properties.

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

      CurrentSituationLaneView ( LaneAccess access, LaneDirectionCategory directionCategory, LaneType type)

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

  - <div id="sdk-for-android-navigate-access" class="section detail">

    ### access

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess" title="class in com.here.sdk.navigation">LaneAccess</a></span> <span class="element-name">access</span>

    </div>

    <div class="block">

    Indicates which vehicle types can access this lane.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-directionCategory" class="section detail">

    ### directionCategory

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-lanedirectioncategory" title="class in com.here.sdk.navigation">LaneDirectionCategory</a></span> <span class="element-name">directionCategory</span>

    </div>

    <div class="block">

    Indicates towards which directions this lane leads.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-type" class="section detail">

    ### type

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-lanetype" title="class in com.here.sdk.navigation">LaneType</a></span> <span class="element-name">type</span>

    </div>

    <div class="block">

    Indicates this lane's properties.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-laneMarkings" class="section detail">

    ### laneMarkings

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-lanemarkings" title="class in com.here.sdk.navigation">LaneMarkings</a></span> <span class="element-name">laneMarkings</span>

    </div>

    <div class="block">

    Indicates the lane markings between the lanes.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-directions" class="section detail">

    ### directions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-navigation-lanedirection" title="enum class in com.here.sdk.navigation">LaneDirection</a>\></span> <span class="element-name">directions</span>

    </div>

    <div class="block">

    Indicates which lane directions are available for this lane.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-directionsOnRoute" class="section detail">

    ### directionsOnRoute

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-navigation-lanedirection" title="enum class in com.here.sdk.navigation">LaneDirection</a>\></span> <span class="element-name">directionsOnRoute</span>

    </div>

    <div class="block">

    Indicates which lane directions are on the route. Following those directions keeps the driver on the route.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-com-here-sdk-navigation-LaneAccess-com-here-sdk-navigation-LaneDirectionCategory-com-here-sdk-navigation-LaneType" class="section detail">

    ### CurrentSituationLaneView

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">CurrentSituationLaneView</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess" title="class in com.here.sdk.navigation">LaneAccess</a> access, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-lanedirectioncategory" title="class in com.here.sdk.navigation">LaneDirectionCategory</a> directionCategory, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-lanetype" title="class in com.here.sdk.navigation">LaneType</a> type)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `access` -

    Indicates which vehicle types can access this lane.

    `directionCategory` -

    Indicates towards which directions this lane leads.

    `type` -

    Indicates this lane's properties.

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

