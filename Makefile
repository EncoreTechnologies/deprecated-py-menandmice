THIS_FILE := $(lastword $(MAKEFILE_LIST))
ROOT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
CI_REPO_PATH ?= $(ROOT_DIR)/ci
CI_REPO_BRANCH ?= master

.PHONY: all
all: .DEFAULT

.PHONY: clean
clean: clean-pyc clean-ci-repo

.PHONY: clean-pyc
clean-pyc:
	@echo
	@echo "==================== clean-pyc ===================="
	@echo
	find . -name 'ci' -prune -or -name '.git' -or -type f -name "*.pyc" | xargs rm

# Clone the ci-repo into the ci/ directory
.PHONY: clone-ci-repo
clone-ci-repo:
	@echo
	@echo "==================== clone-ci-repo ===================="
	@echo
	@if [ ! -d "$(CI_REPO_PATH)" ]; then \
		git clone https://github.com/EncoreTechnologies/ci-python.git --depth 1 --single-branch --branch $(CI_REPO_BRANCH) $(CI_REPO_PATH); \
	else \
		pushd $(CI_REPO_PATH) &> /dev/null; \
		git pull; \
		popd &> /dev/null; \
	fi;

# Clean the ci-repo (calling `make clean` in that directory), then remove the
# ci-repo directory
.PHONY: clean-ci-repo
clean-ci-repo:
	@echo
	@echo "==================== clean-ci-repo ===================="
	@echo
	@if [ -d "$(CI_REPO_PATH)" ]; then \
		make -f $(ROOT_DIR)/ci/Makefile clean; \
	fi;
	rm -rf $(CI_REPO_PATH)

# forward all make targets not found in this makefile to the ci makefile to do
# the actual work (by calling the invoke-ci-makefile target)
# http://stackoverflow.org/wiki/Last-Resort_Makefile_Targets
# Unfortunately the .DEFAULT target doesn't allow for dependencies
# so we have to manually specify all of the steps in this target.
.DEFAULT: 
	$(MAKE) clone-ci-repo
	@echo
	@echo "==================== invoke ci/Makefile (targets: $(MAKECMDGOALS)) ===================="
	@echo
	make -f $(ROOT_DIR)/ci/Makefile $(MAKECMDGOALS)
