---
title: "Metadata (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-metadata"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.core](sdk-for-android-explore-com-here-sdk-core-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.NativeBasecom.here.sdk.core.Metadata →
com.here.NativeBase → com.here.sdk.core.Metadata

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">Metadata</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Holds metadata on behalf of a map item. An instance of this class can
contain metadata items of varying types, such as String, Integer,
Double, GeoCoordinates etc. and can also hold arbitrary metadata types
by the use of the CustomMetadataValue interface.

</div>

</div>

<div class="section summary">

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

      Metadata()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates an instance of this class.

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

  [`CustomMetadataValue`](sdk-for-android-explore-com-here-sdk-core-custommetadatavalue "interface in com.here.sdk.core")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getCustomValue(String key)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Obtains an instance of the CustomMetadataValue class associated with a
  given key.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getDouble(String key)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Obtains a Double value associated with a given key.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`GeoCoordinates`](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getGeoCoordinates(String key)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Obtains a GeoCoordinates value associated with a given key.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getInteger(String key)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Obtains an Integer value associated with a given key.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getString(String key)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Obtains a String value associated with a given key.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`MetadataType`](sdk-for-android-explore-com-here-sdk-core-metadatatype "enum class in com.here.sdk.core")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getType(String key)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Determines the type of a metadata value.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      removeValue(String key)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Removes a metadata key and its associated value.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setCustomValue(String key,
       CustomMetadataValue value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Creates a key:value pair, where the value is a type derived from
  CustomMetadataValue.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setDouble(String key,
       double value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Creates a key:value pair, where the value is of type Double.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setGeoCoordinates(String key,
       GeoCoordinates value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Creates a key:value pair, where the value is of type GeoCoordinates.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setInteger(String key,
       int value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Creates a key:value pair, where the value is of type Integer.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setString(String key,
       String value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Creates a key:value pair, where the value is of type String.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">

- <div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">

  - <div id="sdk-for-android-explore-<init>()" class="section detail">

    ### Metadata

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Metadata</span>()

    </div>

    <div class="block">

    Creates an instance of this class.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-getCustomValue(java.lang.String)"
    class="section detail">

    ### getCustomValue

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[CustomMetadataValue](sdk-for-android-explore-com-here-sdk-core-custommetadatavalue "interface in com.here.sdk.core")</span> <span class="element-name">getCustomValue</span><span class="parameters">(@NonNull
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> key)</span>

    </div>

    <div class="block">

    Obtains an instance of the CustomMetadataValue class associated with
    a given key.

    </div>

    Parameters:  
    `key` -

    The name of the key for which to obtain the value.

    Returns:  
    The value associated with the key.

    </div>

  - <div id="sdk-for-android-explore-getDouble(java.lang.String)"
    class="section detail">

    ### getDouble

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">getDouble</span><span class="parameters">(@NonNull
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> key)</span>

    </div>

    <div class="block">

    Obtains a Double value associated with a given key.

    </div>

    Parameters:  
    `key` -

    The name of the key for which to obtain the value.

    Returns:  
    The value associated with the key.

    </div>

  - <div id="sdk-for-android-explore-getGeoCoordinates(java.lang.String)"
    class="section detail">

    ### getGeoCoordinates

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")</span> <span class="element-name">getGeoCoordinates</span><span class="parameters">(@NonNull
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> key)</span>

    </div>

    <div class="block">

    Obtains a GeoCoordinates value associated with a given key.

    </div>

    Parameters:  
    `key` -

    The name of the key for which to obtain the value.

    Returns:  
    The value associated with the key.

    </div>

  - <div id="sdk-for-android-explore-getInteger(java.lang.String)"
    class="section detail">

    ### getInteger

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a></span> <span class="element-name">getInteger</span><span class="parameters">(@NonNull
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> key)</span>

    </div>

    <div class="block">

    Obtains an Integer value associated with a given key.

    </div>

    Parameters:  
    `key` -

    The name of the key for which to obtain the value.

    Returns:  
    The value associated with the key.

    </div>

  - <div id="sdk-for-android-explore-getString(java.lang.String)"
    class="section detail">

    ### getString

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getString</span><span class="parameters">(@NonNull
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> key)</span>

    </div>

    <div class="block">

    Obtains a String value associated with a given key.

    </div>

    Parameters:  
    `key` -

    The name of the key for which to obtain the value.

    Returns:  
    The value associated with the key.

    </div>

  - <div id="sdk-for-android-explore-getType(java.lang.String)"
    class="section detail">

    ### getType

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[MetadataType](sdk-for-android-explore-com-here-sdk-core-metadatatype "enum class in com.here.sdk.core")</span> <span class="element-name">getType</span><span class="parameters">(@NonNull
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> key)</span>

    </div>

    <div class="block">

    Determines the type of a metadata value. If the type of a metadata
    value associated with a key is not known, this method will enable
    the type to be queried, in order to know which get method to call.
    i.e. getDouble(), getInteger() etc.

    </div>

    Parameters:  
    `key` -

    The name of the key for which to obtain the type.

    Returns:  
    An enumeration describing the type of the value associated with the
    key.

    </div>

  - <div id="sdk-for-android-explore-removeValue(java.lang.String)"
    class="section detail">

    ### removeValue

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeValue</span><span class="parameters">(@NonNull
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> key)</span>

    </div>

    <div class="block">

    Removes a metadata key and its associated value.

    </div>

    Parameters:  
    `key` -

    The name of the key to be removed.

    </div>

  - <div id="sdk-for-android-explore-setCustomValue(java.lang.String,com.here.sdk.core.CustomMetadataValue)"
    class="section detail">

    ### setCustomValue

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCustomValue</span><span class="parameters">(@NonNull
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> key,
    @NonNull
    [CustomMetadataValue](sdk-for-android-explore-com-here-sdk-core-custommetadatavalue "interface in com.here.sdk.core") value)</span>

    </div>

    <div class="block">

    Creates a key:value pair, where the value is a type derived from
    CustomMetadataValue. If the given key already exists, its value will
    be replaced by the new one.

    </div>

    Parameters:  
    `key` -

    The name of the key to be created or replaced.

    `value` -

    The value to be assigned to the key.

    </div>

  - <div id="sdk-for-android-explore-setDouble(java.lang.String,double)"
    class="section detail">

    ### setDouble

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDouble</span><span class="parameters">(@NonNull
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> key,
    double value)</span>

    </div>

    <div class="block">

    Creates a key:value pair, where the value is of type Double. If the
    given key already exists, its value will be replaced by the new one.

    </div>

    Parameters:  
    `key` -

    The name of the key to be created or replaced.

    `value` -

    The value to be assigned to the key.

    </div>

  - <div id="sdk-for-android-explore-setGeoCoordinates(java.lang.String,com.here.sdk.core.GeoCoordinates)"
    class="section detail">

    ### setGeoCoordinates

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setGeoCoordinates</span><span class="parameters">(@NonNull
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> key,
    @NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") value)</span>

    </div>

    <div class="block">

    Creates a key:value pair, where the value is of type GeoCoordinates.
    If the given key already exists, its value will be replaced by the
    new one.

    </div>

    Parameters:  
    `key` -

    The name of the key to be created or replaced.

    `value` -

    The value to be assigned to the key.

    </div>

  - <div id="sdk-for-android-explore-setInteger(java.lang.String,int)"
    class="section detail">

    ### setInteger

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setInteger</span><span class="parameters">(@NonNull
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> key,
    int value)</span>

    </div>

    <div class="block">

    Creates a key:value pair, where the value is of type Integer. If the
    given key already exists, its value will be replaced by the new one.

    </div>

    Parameters:  
    `key` -

    The name of the key to be created or replaced.

    `value` -

    The value to be assigned to the key.

    </div>

  - <div id="sdk-for-android-explore-setString(java.lang.String,java.lang.String)"
    class="section detail">

    ### setString

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setString</span><span class="parameters">(@NonNull
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> key,
    @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> value)</span>

    </div>

    <div class="block">

    Creates a key:value pair, where the value is of type String. If the
    given key already exists, its value will be replaced by the new one.

    </div>

    Parameters:  
    `key` -

    The name of the key to be created or replaced.

    `value` -

    The value to be assigned to the key.

    </div>

  </div>

</div>

