---
title: "EVSEInfo (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-search-evseinfo"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.search](sdk-for-android-explore-com-here-sdk-search-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.search.EVSEInfo

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">EVSEInfo</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Represents an EVSE at the charging point. Note: This is a beta release
of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.

</div>

</div>

<div class="section summary">

- <div id="sdk-for-android-explore-field-summary"
  class="section field-summary">

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

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a>`<`[`EVSECapability`](sdk-for-android-explore-com-here-sdk-ev-evsecapability "enum class in com.here.sdk.ev")`>`

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-search-evseinfo#capabilities"
  class="member-name-link"><code>capabilities</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Capabilities of the EVSE.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a>`<`[`EVChargingConnector`](sdk-for-android-explore-com-here-sdk-search-evchargingconnector "class in com.here.sdk.search")`>`

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-search-evseinfo#connectors"
  class="member-name-link"><code>connectors</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  List of available connectors on the EVSE.

  </div>

  </div>

  <div class="col-first even-row-color">

  [`GeoCoordinates`](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-search-evseinfo#coordinates"
  class="member-name-link"><code>coordinates</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The geographic coordinates of the EVSE.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evseinfo#evseID"
  class="member-name-link"><code>evseID</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Identifier compliant with the EVSE ID from eMI3 standard version V1.0.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-search-evseinfo#floorLevel"
  class="member-name-link"><code>floorLevel</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Floor level on which the EVSE is located.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evseinfo#id"
  class="member-name-link"><code>id</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Human-readable globally unique identifier for the EVSE.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html"
  class="external-link"
  title="class or interface in java.util"><code>Date</code></a>

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-search-evseinfo#lastUpdated"
  class="member-name-link"><code>lastUpdated</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Timestamp when the status of this EVSE was last updated.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a>`<`[`EVSEPaymentSupport`](sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport "enum class in com.here.sdk.ev")`>`

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-search-evseinfo#paymentSupports"
  class="member-name-link"><code>paymentSupports</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  List of payment support functionalities on EVSE for ad-hoc customers
  (without pre-registration).

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-search-evseinfo#physicalReference"
  class="member-name-link"><code>physicalReference</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  A number or string printed on the outside of the EVSE for visual
  identification.

  </div>

  </div>

  <div class="col-first odd-row-color">

  [`EVSEState`](sdk-for-android-explore-com-here-sdk-ev-evsestate "enum class in com.here.sdk.ev")

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evseinfo#status"
  class="member-name-link"><code>status</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Status of the EVSE.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evseinfo#uid"
  class="member-name-link"><code>uid</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Uniquely identifies the EVSE within the CPOs platform (and suboperator
  platforms).

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-constructor-summary"
  class="section constructor-summary">

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

      EVSEInfo()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary"
  class="section method-summary">

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

      equals(Object obj)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      hashCode()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">

- <div id="sdk-for-android-explore-field-detail"
  class="section field-details">

  - <div id="sdk-for-android-explore-uid" class="section detail">

    ### uid

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">uid</span>

    </div>

    <div class="block">

    Uniquely identifies the EVSE within the CPOs platform (and
    suboperator platforms). For example a database ID or the actual
    "EVSE ID". This field can never be changed, modified or renamed.
    This is the 'technical' identification of the EVSE, not to be used
    as 'human readable' identification, use the field id for that.

    </div>

    </div>

  - <div id="sdk-for-android-explore-id" class="section detail">

    ### id

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">id</span>

    </div>

    <div class="block">

    Human-readable globally unique identifier for the EVSE.

    </div>

    </div>

  - <div id="sdk-for-android-explore-evseID" class="section detail">

    ### evseID

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">evseID</span>

    </div>

    <div class="block">

    Identifier compliant with the EVSE ID from eMI3 standard version
    V1.0.

    </div>

    </div>

  - <div id="sdk-for-android-explore-status" class="section detail">

    ### status

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[EVSEState](sdk-for-android-explore-com-here-sdk-ev-evsestate "enum class in com.here.sdk.ev")</span> <span class="element-name">status</span>

    </div>

    <div class="block">

    Status of the EVSE.

    </div>

    </div>

  - <div id="sdk-for-android-explore-lastUpdated"
    class="section detail">

    ### lastUpdated

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html"
    class="external-link" title="class or interface in java.util">Date</a></span> <span class="element-name">lastUpdated</span>

    </div>

    <div class="block">

    Timestamp when the status of this EVSE was last updated.

    </div>

    </div>

  - <div id="sdk-for-android-explore-connectors" class="section detail">

    ### connectors

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[EVChargingConnector](sdk-for-android-explore-com-here-sdk-search-evchargingconnector "class in com.here.sdk.search")></span> <span class="element-name">connectors</span>

    </div>

    <div class="block">

    List of available connectors on the EVSE. An operational EVSE should
    have at least one connector.

    </div>

    </div>

  - <div id="sdk-for-android-explore-capabilities"
    class="section detail">

    ### capabilities

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[EVSECapability](sdk-for-android-explore-com-here-sdk-ev-evsecapability "enum class in com.here.sdk.ev")></span> <span class="element-name">capabilities</span>

    </div>

    <div class="block">

    Capabilities of the EVSE.

    </div>

    </div>

  - <div id="sdk-for-android-explore-floorLevel" class="section detail">

    ### floorLevel

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">floorLevel</span>

    </div>

    <div class="block">

    Floor level on which the EVSE is located.

    </div>

    </div>

  - <div id="sdk-for-android-explore-physicalReference"
    class="section detail">

    ### physicalReference

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">physicalReference</span>

    </div>

    <div class="block">

    A number or string printed on the outside of the EVSE for visual
    identification.

    </div>

    </div>

  - <div id="sdk-for-android-explore-coordinates"
    class="section detail">

    ### coordinates

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")</span> <span class="element-name">coordinates</span>

    </div>

    <div class="block">

    The geographic coordinates of the EVSE.

    </div>

    </div>

  - <div id="sdk-for-android-explore-paymentSupports"
    class="section detail">

    ### paymentSupports

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[EVSEPaymentSupport](sdk-for-android-explore-com-here-sdk-ev-evsepaymentsupport "enum class in com.here.sdk.ev")></span> <span class="element-name">paymentSupports</span>

    </div>

    <div class="block">

    List of payment support functionalities on EVSE for ad-hoc customers
    (without pre-registration).

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">

  - <div id="sdk-for-android-explore-<init>()" class="section detail">

    ### EVSEInfo

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">EVSEInfo</span>()

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-equals(java.lang.Object)"
    class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><span class="parameters">(<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
    class="external-link"
    title="class or interface in java.lang"><code>equals</code></a> in
    class <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link"
    title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-explore-hashCode()" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
    class="external-link"
    title="class or interface in java.lang"><code>hashCode</code></a> in
    class <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link"
    title="class or interface in java.lang"><code>Object</code></a>

    </div>

  </div>

</div>

