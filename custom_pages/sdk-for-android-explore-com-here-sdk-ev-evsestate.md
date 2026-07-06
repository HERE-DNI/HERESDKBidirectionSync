---
title: "EVSEState (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-ev-evsestate"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.ev](sdk-for-android-explore-com-here-sdk-ev-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → java.lang.Enum\<EVSEState\>com.here.sdk.ev.EVSEState
→ java.lang.Enum → EVSEState → com.here.sdk.ev.EVSEState

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

All Implemented Interfaces:  
<a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html"
class="external-link"
title="class or interface in java.io"><code>Serializable</code></a>, <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html"
class="external-link"
title="class or interface in java.lang"><code>Comparable</code></a>`<`[`EVSEState`](sdk-for-android-explore-com-here-sdk-ev-evsestate "enum class in com.here.sdk.ev")`>`,
<a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html"
class="external-link"
title="class or interface in java.lang.constant"><code>Constable</code></a>

<div class="type-signature">

<span class="modifiers">public enum
</span><span class="element-name type-name-label">EVSEState</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html"
class="external-link" title="class or interface in java.lang">Enum</a>\<[EVSEState](sdk-for-android-explore-com-here-sdk-ev-evsestate "enum class in com.here.sdk.ev")\></span>

</div>

<div class="block">

Indicates the current short-term status of the EVSE at the time given in
the modified property. There are no separate statuses available for
individual connectors. A single EVSE can only be used by a single car,
so same statuses apply to other connectors as well. So, if one connector
is in use, the whole EVSE has status charging, and other connectors
cannot be used at the same time, hence they should be considered in-use
as well. If an EVSE can allow multiple connectors to be used at the same
time, it is basically multiple EVSEs merged into a single physical box
or device. Note: This is a beta release of this feature, so there could
be a few bugs and unexpected behaviors. Related APIs may change for new
releases without a deprecation process.

</div>

</div>

<div class="section summary">

- <div id="sdk-for-android-explore-nested-class-summary"
  class="section nested-class-summary">

  <div class="inherited-list">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html"
  class="external-link"
  title="class or interface in java.lang"><code>Enum.EnumDesc</code></a>`<`<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html"
  class="external-link"
  title="class or interface in java.lang"><code>E</code></a>` extends `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html"
  class="external-link"
  title="class or interface in java.lang"><code>Enum</code></a>`<`<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html"
  class="external-link"
  title="class or interface in java.lang"><code>E</code></a>`>>`

  </div>

  </div>

- <div id="sdk-for-android-explore-enum-constant-summary"
  class="section constants-summary">

  <div class="caption">

  Enum Constants

  </div>

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Enum Constant

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-ev-evsestate#AVAILABLE"
  class="member-name-link"><code>AVAILABLE</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The EVSE/connector is able to start a new charging session.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-ev-evsestate#BLOCKED"
  class="member-name-link"><code>BLOCKED</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The EVSE/connector is not accessible because of a physical barrier,
  i.e.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-ev-evsestate#CHARGING"
  class="member-name-link"><code>CHARGING</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The EVSE/connector is in use.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-ev-evsestate#INOPERATIVE"
  class="member-name-link"><code>INOPERATIVE</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The EVSE/connector is temporarily not available for use, but not
  broken or defect.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-ev-evsestate#OPERATIONAL"
  class="member-name-link"><code>OPERATIONAL</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The EVSE/connector was operational when checked the last time, but the
  actual latest status is not available at the moment.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-ev-evsestate#OUT_OF_ORDER"
  class="member-name-link"><code>OUT_OF_ORDER</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The EVSE/connector is currently out of order.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-ev-evsestate#RESERVED"
  class="member-name-link"><code>RESERVED</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The EVSE/connector is reserved for a particular EV driver and is
  unavailable for other drivers.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-ev-evsestate#UNKNOWN"
  class="member-name-link"><code>UNKNOWN</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  No status information available or the EVSE/connector is offline.

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `[`EVSEState`](sdk-for-android-explore-com-here-sdk-ev-evsestate "enum class in com.here.sdk.ev")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      valueOf(String name)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Returns the enum constant of this class with the specified name.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `[`EVSEState`](sdk-for-android-explore-com-here-sdk-ev-evsestate "enum class in com.here.sdk.ev")`[]`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      values()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Returns an array containing the constants of this enum class, in the
  order they are declared.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html"
  class="external-link" title="class or interface in java.lang">Enum</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)"
  class="external-link"
  title="class or interface in java.lang"><code>compareTo</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()"
  class="external-link"
  title="class or interface in java.lang"><code>describeConstable</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)"
  class="external-link"
  title="class or interface in java.lang"><code>equals</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getDeclaringClass</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()"
  class="external-link"
  title="class or interface in java.lang"><code>hashCode</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()"
  class="external-link"
  title="class or interface in java.lang"><code>name</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()"
  class="external-link"
  title="class or interface in java.lang"><code>ordinal</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String)"
  class="external-link"
  title="class or interface in java.lang"><code>valueOf</code></a>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">

- <div id="sdk-for-android-explore-enum-constant-detail"
  class="section constant-details">

  - <div id="sdk-for-android-explore-UNKNOWN" class="section detail">

    ### UNKNOWN

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[EVSEState](sdk-for-android-explore-com-here-sdk-ev-evsestate "enum class in com.here.sdk.ev")</span> <span class="element-name">UNKNOWN</span>

    </div>

    <div class="block">

    No status information available or the EVSE/connector is offline.

    </div>

    </div>

  - <div id="sdk-for-android-explore-AVAILABLE" class="section detail">

    ### AVAILABLE

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[EVSEState](sdk-for-android-explore-com-here-sdk-ev-evsestate "enum class in com.here.sdk.ev")</span> <span class="element-name">AVAILABLE</span>

    </div>

    <div class="block">

    The EVSE/connector is able to start a new charging session.

    </div>

    </div>

  - <div id="sdk-for-android-explore-BLOCKED" class="section detail">

    ### BLOCKED

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[EVSEState](sdk-for-android-explore-com-here-sdk-ev-evsestate "enum class in com.here.sdk.ev")</span> <span class="element-name">BLOCKED</span>

    </div>

    <div class="block">

    The EVSE/connector is not accessible because of a physical barrier,
    i.e. a car.

    </div>

    </div>

  - <div id="sdk-for-android-explore-CHARGING" class="section detail">

    ### CHARGING

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[EVSEState](sdk-for-android-explore-com-here-sdk-ev-evsestate "enum class in com.here.sdk.ev")</span> <span class="element-name">CHARGING</span>

    </div>

    <div class="block">

    The EVSE/connector is in use.

    </div>

    </div>

  - <div id="sdk-for-android-explore-INOPERATIVE"
    class="section detail">

    ### INOPERATIVE

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[EVSEState](sdk-for-android-explore-com-here-sdk-ev-evsestate "enum class in com.here.sdk.ev")</span> <span class="element-name">INOPERATIVE</span>

    </div>

    <div class="block">

    The EVSE/connector is temporarily not available for use, but not
    broken or defect.

    </div>

    </div>

  - <div id="sdk-for-android-explore-OUT_OF_ORDER"
    class="section detail">

    ### OUT_OF_ORDER

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[EVSEState](sdk-for-android-explore-com-here-sdk-ev-evsestate "enum class in com.here.sdk.ev")</span> <span class="element-name">OUT_OF_ORDER</span>

    </div>

    <div class="block">

    The EVSE/connector is currently out of order.

    </div>

    </div>

  - <div id="sdk-for-android-explore-RESERVED" class="section detail">

    ### RESERVED

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[EVSEState](sdk-for-android-explore-com-here-sdk-ev-evsestate "enum class in com.here.sdk.ev")</span> <span class="element-name">RESERVED</span>

    </div>

    <div class="block">

    The EVSE/connector is reserved for a particular EV driver and is
    unavailable for other drivers.

    </div>

    </div>

  - <div id="sdk-for-android-explore-OPERATIONAL"
    class="section detail">

    ### OPERATIONAL

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[EVSEState](sdk-for-android-explore-com-here-sdk-ev-evsestate "enum class in com.here.sdk.ev")</span> <span class="element-name">OPERATIONAL</span>

    </div>

    <div class="block">

    The EVSE/connector was operational when checked the last time, but
    the actual latest status is not available at the moment.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-values()" class="section detail">

    ### values

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">[EVSEState](sdk-for-android-explore-com-here-sdk-ev-evsestate "enum class in com.here.sdk.ev")\[\]</span> <span class="element-name">values</span>()

    </div>

    <div class="block">

    Returns an array containing the constants of this enum class, in the
    order they are declared.

    </div>

    Returns:  
    an array containing the constants of this enum class, in the order
    they are declared

    </div>

  - <div id="sdk-for-android-explore-valueOf(java.lang.String)"
    class="section detail">

    ### valueOf

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">[EVSEState](sdk-for-android-explore-com-here-sdk-ev-evsestate "enum class in com.here.sdk.ev")</span> <span class="element-name">valueOf</span><span class="parameters">(<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> name)</span>

    </div>

    <div class="block">

    Returns the enum constant of this class with the specified name. The
    string must match exactly an identifier used to declare an enum
    constant in this class. (Extraneous whitespace characters are not
    permitted.)

    </div>

    Parameters:  
    `name` - the name of the enum constant to be returned.

    Returns:  
    the enum constant with the specified name

    Throws:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html"
    class="external-link"
    title="class or interface in java.lang"><code>IllegalArgumentException</code></a> -
    if this enum class has no constant with the specified name

    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html"
    class="external-link"
    title="class or interface in java.lang"><code>NullPointerException</code></a> -
    if the argument is null

    </div>

  </div>

</div>

