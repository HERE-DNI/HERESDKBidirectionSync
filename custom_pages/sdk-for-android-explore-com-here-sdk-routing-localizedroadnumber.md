---
title: "LocalizedRoadNumber (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-localizedroadnumber"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.routing.LocalizedRoadNumber → com.here.sdk.routing.LocalizedRoadNumber

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">LocalizedRoadNumber</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Used to represent road number localized to specific language with optional direction and route type information.

</div>

</div>

- <div id="sdk-for-android-explore-field-summary" class="section field-summary">

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

  [`CardinalDirection`](sdk-for-android-explore-com-here-sdk-core-cardinaldirection "enum class in com.here.sdk.core")

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-localizedroadnumber#direction" class="member-name-link"><code>direction</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Road direction.

  </div>

  </div>

  <div class="col-first odd-row-color">

  [`LocalizedText`](sdk-for-android-explore-com-here-sdk-core-localizedtext "class in com.here.sdk.core")

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-localizedroadnumber#localizedNumber" class="member-name-link"><code>localizedNumber</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Road number with locale information.

  </div>

  </div>

  <div class="col-first even-row-color">

  [`RouteType`](sdk-for-android-explore-com-here-sdk-core-routetype "enum class in com.here.sdk.core")

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-localizedroadnumber#routeType" class="member-name-link"><code>routeType</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The route type of the LocalizedRoadNumber.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-constructor-summary" class="section constructor-summary">

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

      LocalizedRoadNumber ( LocalizedText localizedNumber, RouteType routeType)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary" class="section method-summary">

  <div id="sdk-for-android-explore-method-summary-table">

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

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTextWithDirection ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns the whole road number information including its cardinal direction.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      hashCode ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-field-detail" class="section field-details">

  - <div id="sdk-for-android-explore-localizedNumber" class="section detail">

    ### localizedNumber

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[LocalizedText](sdk-for-android-explore-com-here-sdk-core-localizedtext "class in com.here.sdk.core")</span> <span class="element-name">localizedNumber</span>

    </div>

    <div class="block">

    Road number with locale information.

    </div>

    </div>

  - <div id="sdk-for-android-explore-direction" class="section detail">

    ### direction

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type">[CardinalDirection](sdk-for-android-explore-com-here-sdk-core-cardinaldirection "enum class in com.here.sdk.core")</span> <span class="element-name">direction</span>

    </div>

    <div class="block">

    Road direction. This property indicates the official directional identifier assigned to highways. Can be null when direction is not assigned to highways. The direction indicates the same information as on the signpost shield: For example, if is "101 West", the directions contains WEST. Note that the official direction is not necessarily the travel direction. For example, US-101 through the city of Sunnyvale is physically located East to West. However, the official direction on sign is North/South.

    </div>

    </div>

  - <div id="sdk-for-android-explore-routeType" class="section detail">

    ### routeType

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[RouteType](sdk-for-android-explore-com-here-sdk-core-routetype "enum class in com.here.sdk.core")</span> <span class="element-name">routeType</span>

    </div>

    <div class="block">

    The route type of the LocalizedRoadNumber.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-explore-init-com-here-sdk-core-LocalizedText-com-here-sdk-core-RouteType" class="section detail">

    ### LocalizedRoadNumber

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">LocalizedRoadNumber</span><wbr></wbr><span class="parameters">(@NonNull [LocalizedText](sdk-for-android-explore-com-here-sdk-core-localizedtext "class in com.here.sdk.core") localizedNumber, @NonNull [RouteType](sdk-for-android-explore-com-here-sdk-core-routetype "enum class in com.here.sdk.core") routeType)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `localizedNumber` -

    Road number with locale information.

    `routeType` -

    The route type of the LocalizedRoadNumber.

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail" class="section method-details">

  - <div id="sdk-for-android-explore-equals-java-lang-Object" class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr></wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-explore-hashCode" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-explore-getTextWithDirection" class="section detail">

    ### getTextWithDirection

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getTextWithDirection</span>()

    </div>

    <div class="block">

    Returns the whole road number information including its cardinal direction. In case direction is empty, the original localized text will be returned.

    </div>

    Returns:  
    The whole road number information including its cardinal direction.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

