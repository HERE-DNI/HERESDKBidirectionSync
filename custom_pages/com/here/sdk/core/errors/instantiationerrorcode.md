---
title: "InstantiationErrorCode (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestinstantiationerrorcode"
hidden: false
---

Package [com.here.sdk.core.errors](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class InstantiationErrorCode

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[InstantiationErrorCode](sdk-for-android-explore-api-reference-latestinstantiationerrorcode "enum class in com.here.sdk.core.errors")\>
com.here.sdk.core.errors.InstantiationErrorCode
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`InstantiationErrorCode`](sdk-for-android-explore-api-reference-latestinstantiationerrorcode "enum class in com.here.sdk.core.errors")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

------------------------------------------------------------------------
public enum InstantiationErrorCode extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[InstantiationErrorCode](sdk-for-android-explore-api-reference-latestinstantiationerrorcode "enum class in com.here.sdk.core.errors")\>
Instantiation error.

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [ACCESS_KEY_CONTAINS_ILLEGAL_SYMBOL](#ACCESS_KEY_CONTAINS_ILLEGAL_SYMBOL)

Access key contains illegal symbols.

[ACCESS_KEY_SECRET_CONTAINS_ILLEGAL_SYMBOL](#ACCESS_KEY_SECRET_CONTAINS_ILLEGAL_SYMBOL)

Access key secret contains illegal symbols.

[CACHE_FOLDER_ACCESS_DENIED](#CACHE_FOLDER_ACCESS_DENIED)

Access to the specified cache folder is denied

[DATA_FOLDER_ACCESS_DENIED](#DATA_FOLDER_ACCESS_DENIED)

Access to the specified data folder is denied

[FAILED](#FAILED)

Instantiation attempt failed.

[FAILED_TO_CREATE_ANALYTICS_SERVICE](#FAILED_TO_CREATE_ANALYTICS_SERVICE)

Analytics service can not be created

[FAILED_TO_LOCK_CACHE_FOLDER](#FAILED_TO_LOCK_CACHE_FOLDER)

The cache folder for given access key id is locked by other instance of SDKNativeEngine

[ILLEGAL_ARGUMENTS](#ILLEGAL_ARGUMENTS)

Illegal arguments.

[INVALID_CATALOG_CONFIGURATION](#INVALID_CATALOG_CONFIGURATION)

`CatalogConfiguration` contains invalid parameters.

[LAYER_CONFIGURATION_MISMATCH](#LAYER_CONFIGURATION_MISMATCH)

Please check SDKOptions.layerConfiguration against SDK modules configuration.

[PERSISTENT_MAP_STORAGE_FOLDER_ACCESS_DENIED](#PERSISTENT_MAP_STORAGE_FOLDER_ACCESS_DENIED)

Access to the specified persistent map storage folder is denied

[SDK_ENGINE_ALREADY_DISPOSED](#SDK_ENGINE_ALREADY_DISPOSED)

Instantiation attempt failed because the `dispose()` method from `SDKNativeEngine` was called already.

[SHARED_SDK_ENGINE_NOT_INSTANTIATED](#SHARED_SDK_ENGINE_NOT_INSTANTIATED)

Instantiation attempt failed because the shared SDK engine is not instantiated.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`InstantiationErrorCode`](sdk-for-android-explore-api-reference-latestinstantiationerrorcode "enum class in com.here.sdk.core.errors")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`InstantiationErrorCode`](sdk-for-android-explore-api-reference-latestinstantiationerrorcode "enum class in com.here.sdk.core.errors")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### ILLEGAL_ARGUMENTS

public static final [InstantiationErrorCode](sdk-for-android-explore-api-reference-latestinstantiationerrorcode "enum class in com.here.sdk.core.errors") ILLEGAL_ARGUMENTS

    Illegal arguments.

### FAILED

public static final [InstantiationErrorCode](sdk-for-android-explore-api-reference-latestinstantiationerrorcode "enum class in com.here.sdk.core.errors") FAILED

    Instantiation attempt failed. Please check log for error.

### SHARED_SDK_ENGINE_NOT_INSTANTIATED

public static final [InstantiationErrorCode](sdk-for-android-explore-api-reference-latestinstantiationerrorcode "enum class in com.here.sdk.core.errors") SHARED_SDK_ENGINE_NOT_INSTANTIATED

    Instantiation attempt failed because the shared SDK engine is not instantiated. Please initialise the SDK.

### CACHE_FOLDER_ACCESS_DENIED

public static final [InstantiationErrorCode](sdk-for-android-explore-api-reference-latestinstantiationerrorcode "enum class in com.here.sdk.core.errors") CACHE_FOLDER_ACCESS_DENIED

    Access to the specified cache folder is denied

### PERSISTENT_MAP_STORAGE_FOLDER_ACCESS_DENIED

public static final [InstantiationErrorCode](sdk-for-android-explore-api-reference-latestinstantiationerrorcode "enum class in com.here.sdk.core.errors") PERSISTENT_MAP_STORAGE_FOLDER_ACCESS_DENIED

    Access to the specified persistent map storage folder is denied

### FAILED_TO_LOCK_CACHE_FOLDER

public static final [InstantiationErrorCode](sdk-for-android-explore-api-reference-latestinstantiationerrorcode "enum class in com.here.sdk.core.errors") FAILED_TO_LOCK_CACHE_FOLDER

    The cache folder for given access key id is locked by other instance of SDKNativeEngine

### FAILED_TO_CREATE_ANALYTICS_SERVICE

public static final [InstantiationErrorCode](sdk-for-android-explore-api-reference-latestinstantiationerrorcode "enum class in com.here.sdk.core.errors") FAILED_TO_CREATE_ANALYTICS_SERVICE

    Analytics service can not be created

### ACCESS_KEY_CONTAINS_ILLEGAL_SYMBOL

public static final [InstantiationErrorCode](sdk-for-android-explore-api-reference-latestinstantiationerrorcode "enum class in com.here.sdk.core.errors") ACCESS_KEY_CONTAINS_ILLEGAL_SYMBOL

    Access key contains illegal symbols. The below characters are not supported: A. '(single quote) B. "(double quote)

### ACCESS_KEY_SECRET_CONTAINS_ILLEGAL_SYMBOL

public static final [InstantiationErrorCode](sdk-for-android-explore-api-reference-latestinstantiationerrorcode "enum class in com.here.sdk.core.errors") ACCESS_KEY_SECRET_CONTAINS_ILLEGAL_SYMBOL

    Access key secret contains illegal symbols. The below characters are not supported: A. '(single quote) B. "(double quote)

### LAYER_CONFIGURATION_MISMATCH

public static final [InstantiationErrorCode](sdk-for-android-explore-api-reference-latestinstantiationerrorcode "enum class in com.here.sdk.core.errors") LAYER_CONFIGURATION_MISMATCH

    Please check SDKOptions.layerConfiguration against SDK modules configuration.

### SDK_ENGINE_ALREADY_DISPOSED

public static final [InstantiationErrorCode](sdk-for-android-explore-api-reference-latestinstantiationerrorcode "enum class in com.here.sdk.core.errors") SDK_ENGINE_ALREADY_DISPOSED

    Instantiation attempt failed because the `dispose()` method from `SDKNativeEngine` was called already.

### INVALID_CATALOG_CONFIGURATION

public static final [InstantiationErrorCode](sdk-for-android-explore-api-reference-latestinstantiationerrorcode "enum class in com.here.sdk.core.errors") INVALID_CATALOG_CONFIGURATION

    `CatalogConfiguration` contains invalid parameters. Check the corectness of HRNs and versions.

### DATA_FOLDER_ACCESS_DENIED

public static final [InstantiationErrorCode](sdk-for-android-explore-api-reference-latestinstantiationerrorcode "enum class in com.here.sdk.core.errors") DATA_FOLDER_ACCESS_DENIED

    Access to the specified data folder is denied

## Method Details

### values

public static [InstantiationErrorCode](sdk-for-android-explore-api-reference-latestinstantiationerrorcode "enum class in com.here.sdk.core.errors")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [InstantiationErrorCode](sdk-for-android-explore-api-reference-latestinstantiationerrorcode "enum class in com.here.sdk.core.errors") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
