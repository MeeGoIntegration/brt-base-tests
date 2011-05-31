TARGET_PATH=/usr/share/brt-base-tests

all:

clean:

install:
	install -d $(DESTDIR)$(TARGET_PATH)/
	install -m 066 tests.xml $(DESTDIR)$(TARGET_PATH)/
